import os
import math
import timm
import torch
import numpy as np
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score
from utils_init import t2np, get_logp, load_weights
from datasets_init import create_test_data_loader
from models_init import positionalencoding2d, load_flow_model
from visualizer import plot_visualizing_results
from utils import calculate_pro_metric, convert_to_anomaly_test_scores, evaluate_thresholds
from process_log import test_state

def validate(args, data_loader, encoder, decoders):
    
    decoders = [decoder.eval() for decoder in decoders]
    
    image_list, gt_label_list, gt_mask_list, file_names, img_types = [], [], [], [], []
    logps_list = [list() for _ in range(args.feature_levels)]
    with torch.no_grad():
        for i, (image, label, mask, file_name, img_type) in enumerate(data_loader):
            test_state(i,len(data_loader))

            image_list.extend(t2np(image))
            file_names.extend(file_name)
            img_types.extend(img_type)
            gt_label_list.extend(t2np(label))
            gt_mask_list.extend(t2np(mask))
            
            image = image.to(args.device) # single scale
            features = encoder(image)  # BxCxHxW
            
            for l in range(args.feature_levels):
                e = features[l]  # BxCxHxW
                bs, dim, h, w = e.size()
                e = e.permute(0, 2, 3, 1).reshape(-1, dim)
               
                # (bs, 128, h, w)
                pos_embed = positionalencoding2d(args.pos_embed_dim, h, w).to(args.device).unsqueeze(0).repeat(bs, 1, 1, 1)
                pos_embed = pos_embed.permute(0, 2, 3, 1).reshape(-1, args.pos_embed_dim)
                decoder = decoders[l]

                if args.flow_arch == 'flow_model':
                    z, log_jac_det = decoder(e)  
                else:
                    z, log_jac_det = decoder(e, [pos_embed, ])

                logps = get_logp(dim, z, log_jac_det)  
                logps = logps / dim  
                logps_list[l].append(logps.reshape(bs, h, w))
    
    scores, max_values = convert_to_anomaly_test_scores(args, logps_list)
    # calculate detection AUROC
    img_scores = np.max(scores, axis=(1, 2))
    gt_label = np.asarray(gt_label_list, dtype=bool)
    img_auc = roc_auc_score(gt_label, img_scores)
    # calculate segmentation AUROC
    gt_mask = np.squeeze(np.asarray(gt_mask_list, dtype=bool), axis=1)
    pix_auc = roc_auc_score(gt_mask.flatten(), scores.flatten())
    if args.vis:
        img_threshold, pix_threshold = evaluate_thresholds(gt_label, gt_mask, img_scores, scores)
        # save_dir = os.path.join(args.output_dir, args.exp_name, 'vis_results', args.class_name)
        # save_dir = os.path.join('vis_results', args.class_name)
        save_dir = args.heatmap_path
        # os.makedirs(save_dir, exist_ok=True)
        plot_visualizing_results(image_list, scores, img_scores, gt_mask_list, pix_threshold, 
                                 img_threshold, save_dir, file_names, img_types,args)

    
    return img_auc, pix_auc, img_scores, file_names, max_values


def test(args):
    # Feature Extractor
    encoder = timm.create_model(args.backbone_arch, features_only=True, 
                out_indices=[i+1 for i in range(args.feature_levels)], pretrained=True)
    encoder = encoder.to(args.device).eval()
    feat_dims = encoder.feature_info.channels()
    
    # Normalizing Flows
    decoders = [load_flow_model(args, feat_dim) for feat_dim in feat_dims]
    decoders = [decoder.to(args.device) for decoder in decoders]

    # data loaders
    test_loader = create_test_data_loader(args)

    # Load weights(checkpoint)
    load_weights(encoder, decoders, args.checkpoint)

    img_auc, pix_auc, img_scores, file_names, max_values = validate(args, test_loader, encoder, decoders)
    origin_scores = []
    for v in args.val_list:
        origin_scores.append(img_scores[file_names.index(os.path.basename(v[0][:-4]))])
    origin_scores = np.array(origin_scores)
    return img_auc, pix_auc, origin_scores, max_values