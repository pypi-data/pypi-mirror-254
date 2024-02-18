import os
import numpy as np
import torch
import warnings
from config import parse_args
from utils import init_seeds
from PIL import Image

def main_single(device,gpu,input_size,val_list,checkpoint,save_heatmap,save_heatmap_path,heatmap_threshold):
    init_seeds()
    args = parse_args()

    # setting cuda 
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu
    if device == "GPU":
        args.device = torch.device("cuda")
    # model path
    args.model_path = "{}_{}_{}_{}".format(
        args.dataset, args.backbone_arch, args.flow_arch, args.class_name)
    
    # image
    val_sample = Image.open(val_list[0][0])
    args.origin_size = val_sample.size
    # args.img_size = (args.inp_size, args.inp_size)  
    args.img_size = (input_size, input_size)  
    args.crop_size = (input_size, input_size) 
    args.norm_mean, args.norm_std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
    
    args.img_dims = [3] + list(args.img_size)

    # output settings
    args.save_results = True
    args.checkpoint = checkpoint
    args.heatmap_path = save_heatmap_path
    ############################################################################################################################################################
    # set data
    args.train_list = None
    args.val_list = val_list
    args.phase = "test"
    args.vis = save_heatmap
    
    args.heatmap_threshold = heatmap_threshold
    ############################################################################################################################################################
    from bgad_test_engine import test
    img_auc, pix_auc, img_scores, max_values = test(args)
    return img_auc, pix_auc, img_scores, max_values
