import os
import datetime
import numpy as np
from sklearn import manifold
from skimage import morphology
from skimage.segmentation import mark_boundaries
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
# from .utils import *

OUT_DIR = './viz/'
norm = matplotlib.colors.Normalize(vmin=0.0, vmax=255.0)
cm = 1/2.54
dpi = 300

def denormalization(x, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
    mean = np.array(mean)
    std = np.array(std)
    x = (((x.transpose(1, 2, 0) * std) + mean) * 255.).astype(np.uint8)
    return x


def export_hist(c, gts, scores, threshold, postfix='image'):
    print('Exporting histogram...')
    plt.rcParams.update({'font.size': 4})
    image_dirs = os.path.join(OUT_DIR, c.model)
    os.makedirs(image_dirs, exist_ok=True)
    Y = scores.flatten()
    Y_label = gts.flatten()
    fig = plt.figure(figsize=(4*cm, 4*cm), dpi=dpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    fig.add_axes(ax)
    plt.hist([Y[Y_label==1], Y[Y_label==0]], 50, density=True, color=['r', 'g'], label=['ANO', 'TYP'], alpha=0.75, histtype='barstacked')
    plt.axvline(threshold)
    image_file = os.path.join(image_dirs, f'hist_images_{postfix}_' + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
    fig.savefig(image_file, dpi=dpi, format='svg', bbox_inches = 'tight', pad_inches = 0.0)
    plt.close()

def export_groundtruth(c, test_img, gts):
    image_dirs = os.path.join(OUT_DIR, c.model, 'gt_images_' + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
    # images
    if not os.path.isdir(image_dirs):
        print('Exporting grountruth...')
        os.makedirs(image_dirs, exist_ok=True)
        num = len(test_img)
        kernel = morphology.disk(4)
        for i in range(num):
            img = test_img[i]
            img = denormalization(img, c.norm_mean, c.norm_std)
            # gts
            gt_mask = gts[i].astype(np.float64)
            gt_mask = morphology.opening(gt_mask, kernel)
            gt_mask = (255.0*gt_mask).astype(np.uint8)
            gt_img = mark_boundaries(img, gt_mask, color=(1, 0, 0), mode='thick')
            #
            fig = plt.figure(figsize=(2*cm, 2*cm), dpi=dpi)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            ax.imshow(gt_img)
            image_file = os.path.join(image_dirs, '{:08d}'.format(i))
            fig.savefig(image_file, dpi=dpi, format='svg', bbox_inches = 'tight', pad_inches = 0.0)
            plt.close()


def export_scores(c, test_img, scores, threshold):
    image_dirs = os.path.join(OUT_DIR, c.model, 'sc_images_' + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
    # images
    if not os.path.isdir(image_dirs):
        print('Exporting scores...')
        os.makedirs(image_dirs, exist_ok=True)
        num = len(test_img)
        kernel = morphology.disk(4)
        scores_norm = 1.0/scores.max()
        for i in range(num):
            img = test_img[i]
            img = denormalization(img, c.norm_mean, c.norm_std)
            # scores
            score_mask = np.zeros_like(scores[i])
            score_mask[scores[i] >  threshold] = 1.0
            score_mask = morphology.opening(score_mask, kernel)
            score_mask = (255.0*score_mask).astype(np.uint8)
            score_img = mark_boundaries(img, score_mask, color=(1, 0, 0), mode='thick')
            score_map = (255.0*scores[i]*scores_norm).astype(np.uint8)
            #
            fig_img, ax_img = plt.subplots(2, 1, figsize=(2*cm, 4*cm))
            for ax_i in ax_img:
                ax_i.axes.xaxis.set_visible(False)
                ax_i.axes.yaxis.set_visible(False)
                ax_i.spines['top'].set_visible(False)
                ax_i.spines['right'].set_visible(False)
                ax_i.spines['bottom'].set_visible(False)
                ax_i.spines['left'].set_visible(False)
            #
            plt.subplots_adjust(hspace = 0.1, wspace = 0.1)
            ax_img[0].imshow(img, cmap='gray', interpolation='none')
            ax_img[0].imshow(score_map, cmap='jet', norm=norm, alpha=0.5, interpolation='none')
            ax_img[1].imshow(score_img)
            image_file = os.path.join(image_dirs, '{:08d}'.format(i))
            fig_img.savefig(image_file, dpi=dpi, format='svg', bbox_inches = 'tight', pad_inches = 0.0)
            plt.close()


def export_test_images(c, test_img, gts, scores, threshold):
    image_dirs = os.path.join(OUT_DIR, c.model, 'images_' + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
    cm = 1/2.54
    # images
    if not os.path.isdir(image_dirs):
        print('Exporting images...')
        os.makedirs(image_dirs, exist_ok=True)
        num = len(test_img)
        font = {'family': 'serif', 'color': 'black', 'weight': 'normal', 'size': 8}
        kernel = morphology.disk(4)
        scores_norm = 1.0/scores.max()
        for i in range(num):
            img = test_img[i]
            img = denormalization(img, c.norm_mean, c.norm_std)
            # gts
            gt_mask = gts[i].astype(np.float64)
            print('GT:', i, gt_mask.sum())
            gt_mask = morphology.opening(gt_mask, kernel)
            gt_mask = (255.0*gt_mask).astype(np.uint8)
            gt_img = mark_boundaries(img, gt_mask, color=(1, 0, 0), mode='thick')
            # scores
            score_mask = np.zeros_like(scores[i])
            score_mask[scores[i] >  threshold] = 1.0
            print('SC:', i, score_mask.sum())
            score_mask = morphology.opening(score_mask, kernel)
            score_mask = (255.0*score_mask).astype(np.uint8)
            score_img = mark_boundaries(img, score_mask, color=(1, 0, 0), mode='thick')
            score_map = (255.0*scores[i]*scores_norm).astype(np.uint8)
            #
            fig_img, ax_img = plt.subplots(3, 1, figsize=(2*cm, 6*cm))
            for ax_i in ax_img:
                ax_i.axes.xaxis.set_visible(False)
                ax_i.axes.yaxis.set_visible(False)
                ax_i.spines['top'].set_visible(False)
                ax_i.spines['right'].set_visible(False)
                ax_i.spines['bottom'].set_visible(False)
                ax_i.spines['left'].set_visible(False)
            #
            plt.subplots_adjust(hspace = 0.1, wspace = 0.1)
            ax_img[0].imshow(gt_img)
            ax_img[1].imshow(score_map, cmap='jet', norm=norm)
            ax_img[2].imshow(score_img)
            image_file = os.path.join(image_dirs, '{:08d}'.format(i))
            fig_img.savefig(image_file, dpi=dpi, format='svg', bbox_inches = 'tight', pad_inches = 0.0)
            plt.close()


def plot_visualizing_results(test_imgs, scores, img_scores, gt_masks, pixel_threshold, img_threshold, save_dir, file_names, img_types,args):
    """
    Args:
        test_imgs (ndarray): shape (N, 3, h, w)
        scores (ndarray): shape (N, h, w)
        img_scores (ndarray): shape (N, )
        gt_masks (ndarray): shape (N, 1, h, w)
    """
    heat_map_threshold = args.heatmap_threshold
    vmax = scores.max() * 255.
    vmin = scores.min() * 255. + 280
    vmax = vmax + 100
    #vmin = vmax * 0.5 + vmin * 0.5 + 200
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    # norm = matplotlib.colors.Normalize(vmin=0, vmax=255)
    for i in range(len(scores)):
        img = test_imgs[i]
        img = denormalization(img)
        gt_mask = gt_masks[i].squeeze()
        score = scores[i]
        # if score.max() > img_threshold:
        #     score = gaussian_filter(score, sigma=4)
        # else:
        #     score = gaussian_filter(score, sigma=16)
        #     #score[score < img_threshold] = 0
        
        heat_map = score * 255
        mask = score
        # earse the noise heat map point
        # heat_map[mask <= pixel_threshold] = 0
        # heat_map[heat_map <= 127] = 0
        
        mask[mask > pixel_threshold] = 1
        mask[mask <= pixel_threshold] = 0
        kernel = morphology.disk(16)
        mask = morphology.opening(mask, kernel)
        mask *= 255

        fig = plt.figure(figsize=(args.origin_size[0]*0.001, args.origin_size[1]*0.001), dpi=1000)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        
        mean = np.mean(heat_map)
        std_dev = np.std(heat_map)
        heat_map = (heat_map - mean) / std_dev * 255
        
        # heat_map = heat_map.astype(np.uint8)
        heat_map = Image.fromarray(heat_map)
        heat_map = heat_map.resize((args.origin_size[0], args.origin_size[1]))
        heat_map = np.array(heat_map)
        
        vmean = (vmin+vmax)/2
        trans_hmthold = vmean*heat_map_threshold/127.5
        
        heat_map = np.where(heat_map>trans_hmthold,heat_map,0)
        
        img = Image.fromarray(img)
        img = img.resize((args.origin_size[0], args.origin_size[1]))
        img = np.array(img)
        
        ax.imshow(heat_map, cmap='OrRd', norm=norm,interpolation='none')
        ax.imshow(img, cmap='gray', alpha=0.7, interpolation='none')
        fig.savefig(os.path.join(save_dir, file_names[i] + '.png'), dpi=1000)
        plt.close()
        # ###
        # os.makedirs(os.path.join(save_dir, 'normal_ok'), exist_ok=True)
        # os.makedirs(os.path.join(save_dir, 'normal_nok'), exist_ok=True)
        # os.makedirs(os.path.join(save_dir, 'anomaly_ok'), exist_ok=True)
        # os.makedirs(os.path.join(save_dir, 'anomaly_nok'), exist_ok=True)
        # if img_types[i] == 'good':
        #     if img_scores[i] <= img_threshold:
        #         fig.savefig(os.path.join(save_dir, 'normal_ok', img_types[i] + '_' + file_names[i] + '.png'), dpi=1000)
        #     else:
        #         fig.savefig(os.path.join(save_dir, 'normal_nok', img_types[i] + '_' + file_names[i] + '.png'), dpi=1000)
        # else:
        #     if img_scores[i] > img_threshold:
        #         fig.savefig(os.path.join(save_dir, 'anomaly_ok', img_types[i] + '_' + file_names[i] + '.png'), dpi=1000)
        #     else:
        #         fig.savefig(os.path.join(save_dir, 'anomaly_nok', img_types[i] + '_' + file_names[i] + '.png'), dpi=1000)
        # ###
        # plt.close()

def plot_visualizing_inference_results(numpy_image,save_name, scores , save_dir, file_names, args):
    """
    Args:
        test_imgs (ndarray): shape (N, 3, h, w)
        scores (ndarray): shape (N, h, w)
        img_scores (ndarray): shape (N, )
        gt_masks (ndarray): shape (N, 1, h, w)
    """
    heat_map_threshold = args.heatmap_threshold
    vmax = scores.max() * 255.
    vmin = scores.min() * 255. + 280
    vmax = vmax + 100
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    
    score = scores

    heat_map = score * 255
    
    fig = plt.figure(figsize=(args.origin_size[0]*0.001, args.origin_size[1]*0.001), dpi=1000)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    mean = np.mean(heat_map)
    std_dev = np.std(heat_map)
    heat_map = (heat_map - mean) / std_dev * 255
    
    # heat_map = heat_map.astype(np.uint8)
    heat_map = Image.fromarray(heat_map)
    heat_map = heat_map.resize((args.origin_size[0], args.origin_size[1]))
    heat_map = np.array(heat_map)
    
    vmean = (vmin+vmax)/2
    trans_hmthold = vmean*heat_map_threshold/127.5
    
    heat_map = np.where(heat_map>trans_hmthold,heat_map,0)
    
    # heat_map = torch.where(heat_map>trans_hmthold,heat_map,torch.tensor(0.))
    heat_map = (heat_map - vmin) / (vmax - vmin)
    heat_map = heat_map.astype(np.uint8)
    
    heat_map = Image.fromarray(heat_map)

    heat_map = heat_map.resize((args.origin_size[0], args.origin_size[1]))
    # image.save(os.path.join(save_dir, save_name + '.jpg'),"JPEG")
    
    img = Image.fromarray(numpy_image)
    img = img.resize((args.origin_size[0], args.origin_size[1]))
    # img = np.array(img)
    
    # 32x32 검은 이미지
    data = np.zeros([args.origin_size[0], args.origin_size[1], 3], dtype=np.uint8)
    # red_color_image = Image.fromarray(data, 'RGB')
    # 빨간 이미지 
    data[:, :] = [255, 0, 0]
    red_color_image = Image.fromarray(data, 'RGB')
    
    
    im = Image.composite(img, red_color_image, heat_map)
    
    im.save(os.path.join(save_dir, save_name + '.jpg'),"JPEG")
    
    
    # ax.imshow(heat_map, cmap='OrRd', norm=norm,interpolation='none')
    # ax.imshow(img, cmap='gray', alpha=0.7, interpolation='none')
    # fig.savefig(os.path.join(save_dir, save_name + '.png'), dpi=1000)
    # plt.close()

def plot_embedding(feats_1, feats_2, mask, class_name):
    x_min, x_max = np.min(feats_1, 0), np.max(feats_1, 0)
    feats_1 = (feats_1 - x_min) / (x_max - x_min)
    x_min, x_max = np.min(feats_2, 0), np.max(feats_2, 0)
    feats_2 = (feats_1 - x_min) / (x_max - x_min)
    
    plt.style.use('seaborn')
    fig, axs = plt.subplots(1, 2, figsize=(6, 3))
    axs[0].scatter(feats_1[mask == 0, 0], feats_1[mask == 0, 1], color='green')
    axs[0].scatter(feats_1[mask == 1, 1], feats_1[mask == 1, 1], color='red')

    axs[1].scatter(feats_2[mask == 0, 0], feats_2[mask == 0, 1], color='green')
    axs[1].scatter(feats_2[mask == 1, 1], feats_2[mask == 1, 1], color='red')
    
    #axs[0].set_xticks([]), axs[0].set_yticks([])
    #axs[1].set_xticks([]), axs[1].set_yticks([])
    fig.suptitle('t-SNE plot')
    plt.savefig(f't_sne_{class_name}.jpg')
    #plt.show()


def plot_t_sne(feats_1, feats_2, mask, class_name):
    feats_1 = feats_1.reshape(-1, feats_1.shape[-1])
    feats_2 = feats_2.reshape(-1, feats_2.shape[-1])
    mask = mask.reshape(-1)
    tsne_1 = manifold.TSNE(n_components=2, init='pca', random_state=0)
    tsne_2 = manifold.TSNE(n_components=2, init='pca', random_state=0)
    feats_1_tsne = tsne_1.fit_transform(feats_1)
    feats_2_tsne = tsne_2.fit_transform(feats_2)
    plot_embedding(feats_1_tsne, feats_2_tsne, mask, class_name)