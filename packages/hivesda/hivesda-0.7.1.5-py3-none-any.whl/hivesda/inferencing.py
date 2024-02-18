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
from visualizer import plot_visualizing_inference_results
from utils import calculate_pro_metric, convert_to_anomaly_scores, evaluate_thresholds,convert_to_anomaly_inference_scores
from process_log import test_state
from config import parse_args
from utils import init_seeds
from PIL import Image
import torchvision.transforms as transforms

def validate(args, numpy_image, save_name,encoder, decoders,max_values):
    
    decoders = [decoder.eval() for decoder in decoders]
    
    image_list, gt_label_list, gt_mask_list, file_names, img_types = [], [], [], [], []
    logps_list = [list() for _ in range(args.feature_levels)]
    with torch.no_grad():
        
        # img = Image.open(image_path)
        img = Image.fromarray(numpy_image)
        preprocess = transforms.Compose([
            transforms.Resize(args.img_size,Image.ANTIALIAS),
            transforms.ToTensor(),
        ])
        normalize = transforms.Compose([transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
        
        input_tensor = normalize(preprocess(img))
        img = input_tensor.unsqueeze(0)
        
        image = img.to(args.device) # single scale
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
    
    scores = convert_to_anomaly_inference_scores(args, logps_list,max_values)
    # calculate detection AUROC
    img_scores = np.max(scores)
    if args.vis:
        # img_threshold, pix_threshold = evaluate_thresholds(gt_label, gt_mask, img_scores, scores)
        # save_dir = os.path.join(args.output_dir, args.exp_name, 'vis_results', args.class_name)
        # save_dir = os.path.join('vis_results', args.class_name)
        save_dir = args.heatmap_path
        # os.makedirs(save_dir, exist_ok=True)
        plot_visualizing_inference_results(numpy_image,save_name, scores, save_dir, file_names, args)
    
    return img_scores


def start_inference(device,gpu,numpy_image,save_name,encoder,decoders,input_size,save_heatmap,heatmap_threshold,save_heatmap_path,max_values):
    args = parse_args()
    if device == "GPU":
        args.device = torch.device("cuda")
    args.img_size = (input_size,input_size)
    args.crop_size = (input_size, input_size) 
    args.norm_mean, args.norm_std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
    args.img_dims = [3] + list(args.img_size)
    args.vis = save_heatmap
    # data loaders
    # test_loader = create_test_data_loader(args)
    args.heatmap_threshold = heatmap_threshold
    args.heatmap_path = save_heatmap_path
    
    val_sample = Image.fromarray(numpy_image)
    args.origin_size = val_sample.size
    
    
    img_scores = validate(args, numpy_image,save_name, encoder, decoders,max_values)
    
    return img_scores

def load_model(device,gpu,checkpoint):
    init_seeds()
    args = parse_args()
    args.checkpoint = checkpoint
    
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu
    if device == "GPU":
        args.device = torch.device("cuda")
        
    encoder = timm.create_model(args.backbone_arch, features_only=True, 
                out_indices=[i+1 for i in range(args.feature_levels)], pretrained=True)
    encoder = encoder.to(args.device).eval()
    feat_dims = encoder.feature_info.channels()
    
    # Normalizing Flows
    decoders = [load_flow_model(args, feat_dim) for feat_dim in feat_dims]
    decoders = [decoder.to(args.device) for decoder in decoders]
    
    load_weights(encoder, decoders, args.checkpoint)
    
    return encoder,decoders