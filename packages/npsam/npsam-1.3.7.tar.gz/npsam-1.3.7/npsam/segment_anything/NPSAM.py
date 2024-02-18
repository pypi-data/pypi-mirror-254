# Standard library imports
import os, re, sys
from pathlib import Path
from time import time

# Third-party imports
import cv2
import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numba as nb
import numpy as np
import pandas as pd
import skimage
import torch
import math
import tifffile
import json
import requests
import NPSAM
from tqdm import tqdm
from FastSAM import FastSAM, FastSAMPrompt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.widgets import Button, RadioButtons, RangeSlider, Slider
from PyQt5.QtWidgets import QFileDialog, QApplication
from numba import njit, objmode
from numba.extending import overload, register_jitable
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator
from skimage.measure import label, regionprops_table, regionprops
from datetime import datetime

# Clean up
import gc
print('hej')

def get_file_path(directory='./'):
    app = QApplication(sys.argv)
    fname = QFileDialog.getOpenFileNames(None, "Select a file...", directory,
                                         filter="Image files (*.png *.jpg *.jpeg *.tif *.tiff);;All files (*)")
    print(f'filepath = {fname[0]}'.replace(', ', ',\n'))
    return fname[0]


def get_folder_path(directory='./'):
    app = QApplication([])
    folder = QFileDialog.getExistingDirectory(None, "Select a folder...", directory)
    print(f'filepath = "{folder}"')
    return folder


def process_filepath(filepath):
    if type(filepath) == str:
        filepath = Path(filepath).absolute()

        if filepath.is_file():
            if filepath.suffix in {'.png', '.jpg', '.tif', '.tiff'}:
                list_of_images = [filepath.as_posix()]
            else:
                print('Error: File must be .png, .jpg, .tif or .tiff')
                return None
        elif filepath.is_dir():
            folder_content = [filepath / filename for filename in os.listdir(filepath)]
            list_of_images = [filename.as_posix() for filename in folder_content
                              if filename.suffix in {'.png', '.jpg', '.tif', '.tiff'}]
        else:
            print('Error: The string did not contain a path to a folder or an image.')

    elif type(filepath) == list:
        for filename in filepath:
            if not Path(filename).is_file():
                print(
                    f'Error: Not all list entries are valid filenames. \nThe issue is: {Path(filename).as_posix()} \nINFO: Folder paths should be given as a string, not a list.')
                return None
        list_of_images = [Path(filename).absolute().as_posix() for filename in filepath
                          if Path(filename).suffix in {'.png', '.jpg', '.tif', '.tiff'}]
    else:
        print('Unexpected error')
        return None

    return list_of_images


def load_image(filepath):
    if Path(filepath).suffix in {'.tif', '.tiff'}:
        im = tifffile.imread(filepath)
        im_shift_to_zero = im - im.min()
        im_max = im_shift_to_zero.max()
        im_normalized = im_shift_to_zero / im_max
        im_max_255 = im_normalized * 255
        im_8bit = im_max_255.astype('uint8')
        im_RGB = np.dstack([im_8bit] * 3)
    elif Path(filepath).suffix in {'.png', '.jpg'}:
        im = cv2.imread(filepath)
        im_RGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return im_RGB


def make_randomized_cmap(cmap='viridis', seed=42):
    '''Genarates randomized colormap with the first color being black'''
    cmap = matplotlib.colormaps[cmap]
    cmap_colors = cmap(np.linspace(0, 1, 2000))
    black_color = np.array([0, 0, 0, 1])
    cmap_rest_colors = cmap_colors[1:, :]
    np.random.seed(seed)
    np.random.shuffle(cmap_rest_colors)
    randomized_cmap = matplotlib.colors.ListedColormap(np.vstack((np.expand_dims(black_color, 0), cmap_rest_colors)))
    return randomized_cmap


def preprocess(filepath, crop_and_enlarge=False, invert=False):
    image = load_image(filepath)
    files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')

    filename = Path(filepath).stem
    if invert:
        image = cv2.bitwise_not(image)
        filename += '_invert'
    if crop_and_enlarge:
        imshapex = image.shape[0]
        imshapey = image.shape[1]

        crop1 = np.kron(image[:int((imshapex / 2) * 1.25), : int((imshapey / 2) * 1.25), :], np.ones((2, 2, 1)))
        crop2 = np.kron(image[math.ceil((imshapex / 2) * 0.75):, :int((imshapey / 2) * 1.25), :], np.ones((2, 2, 1)))
        crop3 = np.kron(image[:int((imshapex / 2) * 1.25), math.ceil((imshapey / 2) * 0.75):, :], np.ones((2, 2, 1)))
        crop4 = np.kron(image[math.ceil((imshapex / 2) * 0.75):, math.ceil((imshapey / 2) * 0.75):, :],
                        np.ones((2, 2, 1)))
        images = [crop1, crop2, crop3, crop4]
        filenames = [filename + '_crop' + str(number) + '.png' for number in [1, 2, 3, 4]]
    else:
        filenames = [filename + '.png']
        images = [image]

    for image, filename in zip(images, filenames):
        cv2.imwrite((files_folder / filename).as_posix(), image)

    return [(files_folder / filename).as_posix() for filename in filenames]


def find_array_of_bboxes_and_rearrange_masks(filepath, image_filepaths):
    files_folder = Path(image_filepaths[0]).parent

    image = load_image(filepath)

    for image_filepath in image_filepaths:
        file_p = files_folder / (Path(image_filepath).stem + '_array_of_masks.npz')
        array_of_masks = np.load(file_p)['array']
        list_of_bbox = []
        for mask in np.moveaxis(array_of_masks, -1, 0):
            if mask.sum() > 0:
                list_of_bbox.append(regionprops(mask.astype('uint16'))[0]['bbox'])

        imx = image.shape[0]
        imy = image.shape[1]
        dx = 2 * math.ceil(imx / 2 * 0.75)
        dy = 2 * math.ceil(imy / 2 * 0.75)

        dx_min = imx * 2 - int(imx * 1.25)
        dy_min = imy * 2 - int(imy * 1.25)
        dx_max = imx * 2 - math.ceil(imx * 0.75)
        dy_max = imy * 2 - math.ceil(imy * 0.75)

        list_of_bbox2 = []
        list_of_rearranged_masks = []
        for bbox, mask in zip(list_of_bbox, np.moveaxis(array_of_masks, -1, 0)):
            x_min = bbox[0]
            y_min = bbox[1]
            x_max = bbox[2]
            y_max = bbox[3]
            if image_filepath[-5] in {'2', '4'}:
                x_min += dx
                x_max += dx
            if image_filepath[-5] in {'3', '4'}:
                y_min += dy
                y_max += dy
            list_of_bbox2.append([x_min, y_min, x_max, y_max])

            new_mask = np.zeros((imx * 2, imy * 2))
            if image_filepath[-5] == '1':
                new_mask[:mask.shape[0], :mask.shape[1]] = mask
            if image_filepath[-5] == '2':
                new_mask[-mask.shape[0]:, :mask.shape[1]] = mask
            if image_filepath[-5] == '3':
                new_mask[:mask.shape[0], -mask.shape[1]:] = mask
            if image_filepath[-5] == '4':
                new_mask[-mask.shape[0]:, -mask.shape[1]:] = mask
            list_of_rearranged_masks.append(new_mask)

        array_of_masks = np.stack(list_of_rearranged_masks, axis=-1)
        file_p = files_folder / (Path(image_filepath).stem + '_array_of_masks_rearranged.npz')
        np.savez_compressed(file_p, array=array_of_masks)
        array_of_bbox = np.array(list_of_bbox2)
        file_p = files_folder / (Path(image_filepath).stem + '_array_of_bbox.npz')
        np.savez_compressed(file_p, array=array_of_bbox)


def bb_iou(boxA, boxB):
    xA = np.maximum(boxA[0], boxB[0])
    yA = np.maximum(boxA[1], boxB[1])
    xB = np.minimum(boxA[2], boxB[2])
    yB = np.minimum(boxA[3], boxB[3])

    interArea = np.maximum(0, xB - xA) * np.maximum(0, yB - yA)

    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / (boxAArea + boxBArea - interArea)

    return iou


def split_list(to_keep, split_conditions):
    start = 0
    result = []
    for split in split_conditions:
        while split not in to_keep:
            split += 1
        idx = to_keep.index(split)
        result.append(to_keep[start:idx])
        start = idx
    result.append(to_keep[start:])
    return result


def remove_overlapping_bb(image_filepaths, iou_threshold=0.9):
    files_folder = Path(image_filepaths[0]).parent
    all_bboxes = []
    all_masks = []
    split = []

    # Load bounding boxes from .npz files
    for image_filepath in image_filepaths:
        bboxes = np.load(files_folder / (Path(image_filepath).stem + '_array_of_bbox.npz'))['array']
        all_bboxes.append(bboxes)
        array_of_masks = np.load(files_folder / (Path(image_filepath).stem + '_array_of_masks_rearranged.npz'))['array']
        for mask in np.moveaxis(array_of_masks, -1, 0):
            all_masks.append(mask)

    all_bboxes = np.vstack(all_bboxes)

    all_masks = np.stack(all_masks, axis=-1)

    # This will store the indices of the bboxes to keep
    to_keep = []

    for i, boxA in enumerate(all_bboxes):
        keep = True
        for j, boxB in enumerate(all_bboxes):
            if i != j:
                iou = bb_iou(boxA, boxB)
                if iou >= iou_threshold:
                    if i not in to_keep and j not in to_keep:
                        to_keep.append(i)
                    keep = False
                    break
        if keep:
            to_keep.append(i)

    unique_bboxes = all_bboxes[to_keep]
    unique_masks = all_masks[:, :, to_keep]

    print(f'{len(all_bboxes) - len(unique_bboxes)} masks have been removed because they were indentical.')

    return unique_masks


def bin_masks(filepath, unique_masks, binning=True):
    image = load_image(filepath)
    files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')

    if binning:
        if unique_masks.shape[0] % 2 or unique_masks.shape[1] % 2:
            raise ValueError("The first and second dimensions of the array must be even for 2x2 binning.")

        # Define new shape and strides for the view that groups elements into 2x2 blocks
        new_shape = (unique_masks.shape[0] // 2, unique_masks.shape[1] // 2, 2, 2, unique_masks.shape[2])
        new_strides = (unique_masks.strides[0] * 2, unique_masks.strides[1] * 2) + unique_masks.strides

        # Create a strided array of 2x2 blocks
        strided = np.lib.stride_tricks.as_strided(unique_masks, shape=new_shape, strides=new_strides)

        # Perform logical OR on the blocks across the last two dimensions which are the original 2x2
        binned = np.logical_or.reduce(strided, axis=(2, 3))

        np.savez_compressed(files_folder / (Path(filepath).stem + '_array_of_masks.npz'), array=binned.astype(int))
        print(f'An array with shape {binned.astype(int).shape} has been saved.')

    else:
        np.savez_compressed(files_folder / (Path(filepath).stem + '_array_of_masks.npz'), array=new_mask_array)
        print(f'An array with shape {new_mask_array.shape} has been saved.')


def stitch_crops_together(filepath, image_filepaths_raw, iou_threshold=0.9):
    image_filepaths = []
    for image_filepath in image_filepaths_raw:
        if Path(image_filepath.replace('.png', '_array_of_masks.npz')).is_file():
            image_filepaths.append(image_filepath)

    print('Finding bounding boxes and rearranging masks.', end=' ')
    find_array_of_bboxes_and_rearrange_masks(filepath, image_filepaths)
    print('Done.')
    print('Removing masks with identical bounding boxes.')
    unique_masks = remove_overlapping_bb(image_filepaths, iou_threshold=iou_threshold)
    print('Done.')
    print('Creating the final array of masks.')
    bin_masks(filepath, unique_masks)


def format_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    time_string = ""
    if minutes >= 1:
        minute_label = "minute" if minutes == 1 else "minutes"
        time_string += f"{int(minutes)} {minute_label} and "
    second_label = "second" if seconds == 1 else "seconds"
    time_string += f"{round(seconds)} {second_label}"
    return time_string


def download_weights(model):
    weights = {
        'huge': ['https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth', 'sam_vit_h_4b8939.pth'],
        'large': ['https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth', 'sam_vit_l_0b3195.pth'],
        'base': ['https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth', 'sam_vit_b_01ec64.pth'],
        'FastSAM': ['https://drive.google.com/u/0/uc?id=1m1sjY4ihXBU1fZXdQ-Xdj-mDltW-2Rqv&export=download&confirm=' \
                    't&uuid=bacf82f5-6461-44a5-8594-e534dd1b0509&at=AB6BwCD_YbFjLvGr0XiZVPtCQieh:1703072969660',
                    'FastSAM.pt']
    }
    directory = os.path.dirname(NPSAM.__file__)

    if not os.path.exists(directory):
        print('NP-SAM is not correctly installed')
        return

    file_path = os.path.join(directory, weights.get(model)[1])
    try:
        response = requests.get(weights.get(model)[0], stream=True)
        response.raise_for_status()

        total_length = int(response.headers.get('content-length', 0))

        with open(file_path, 'wb') as file, tqdm(
                desc=weights.get(model)[1], total=total_length, unit='iB', unit_scale=True,
                unit_divisor=1024, file=sys.stdout, colour='GREEN', dynamic_ncols=True,
                smoothing=0.1) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
        print(f"File downloaded successfully: {file_path}")
    except requests.RequestException as e:
        print(f"Failed to download {weights.get(model)[1]}: {e}")


def choose_SAM_model(SAM_model):
    model_mapping = {'b': 'base', 'l': 'large', 'h': 'huge'}
    SAM_model = model_mapping.get(SAM_model.lower(), SAM_model)

    directory = os.path.dirname(NPSAM.__file__)
    available_SAM_models = set(os.listdir(directory)) | set(os.listdir())

    model_types = {'huge': ['vit_h', 'h_4b8939'], 'large': ['vit_l', 'l_0b3195'], 'base': ['vit_b', 'b_01ec64']}
    SAM_model = SAM_model.lower()

    if SAM_model == 'auto':
        for model, type_name in model_types.items():
            checkpoint_file = f'sam_vit_{type_name[1]}.pth'
            if any(fname.startswith(checkpoint_file) for fname in available_SAM_models):
                print(f'The SAM weight {type_name[0]} was chosen')
                return os.path.join(directory, f'sam_vit_{type_name[1]}.pth'), type_name[0]
    elif SAM_model in {'base', 'large', 'huge'}:
        checkpoint_file = f'sam_vit_{model_types.get(SAM_model)[1]}.pth'
        if any(fname.startswith(checkpoint_file) for fname in available_SAM_models):
            return os.path.join(directory, f'sam_vit_{model_types.get(SAM_model)[1]}.pth'), model_types.get(SAM_model)[
                0]
        else:
            _input = input(
                f'The SAM weight {model_types[SAM_model][0]} was not found. Do you want to download it? y/n: ')
            if _input.lower() == 'y':
                download_weights(SAM_model)
                return os.path.join(directory, f'sam_vit_{model_types.get(SAM_model)[1]}.pth'), \
                       model_types.get(SAM_model)[0]
    else:
        print("Invalid input. Valid inputs are 'auto', 'h' for huge, 'l' for large, and 'b' for base.")
        return None

    # Handle 'auto' case when no models are found
    if not os.path.exists(os.path.join(directory, 'sam_vit_b_01ec64.pth')) and not os.path.exists(
            os.path.join(directory, 'sam_vit_l_0b3195.pth')) and not os.path.exists(
            os.path.join(directory, 'sam_vit_h_4b8939.pth')):
        _input = input('No SAM weights were found. Do you want to download the huge? y/n: ')
        if _input.lower() == 'y':
            download_weights('huge')
            return os.path.join(directory, 'sam_vit_h_4b8939.pth'), 'vit_h'
        else:
            return None
    elif os.path.exists(os.path.join(directory, 'sam_vit_h_4b8939.pth')):
        _input = input('The huge weight is downloaded found. Do you want to use it instead? y/n: ')
        if _input.lower() == 'y':
            return os.path.join(directory, 'sam_vit_h_4b8939.pth'), 'vit_h'
        else:
            return None
    elif os.path.exists(os.path.join(directory, 'sam_vit_l_0b3195.pth')):
        _input = input('The large weight is downloaded found. Do you want to use it instead? y/n: ')
        if _input.lower() == 'y':
            return os.path.join(directory, 'sam_vit_l_0b3195.pth'), 'vit_l'
        else:
            return None
    elif os.path.exists(os.path.join(directory, 'sam_vit_b_01ec64.pth')):
        _input = input('The base weight is downloaded found. Do you want to use it instead? y/n: ')
        if _input.lower() == 'y':
            return os.path.join(directory, 'sam_vit_b_01ec64.pth'), 'vit_b'
        else:
            return None


def SAM(filepath, device='cpu', PPS=64, prefilter=True, min_mask_region_area=35, SAM_model='auto',
        crop_and_enlarge=False, invert=False, **kwargs):
    '''SAM makes masks of the image
    Takes an image as input given as a filepath.
    Device can be default:'cpu' or 'cuda'
    PPS (points per side) number of sampling points default 64
    Saves the masks as a compressed numpy array file to easier load it later
    '''
    filepaths = process_filepath(filepath)

    for filepath in filepaths:
        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')
        files_folder.mkdir(exist_ok=True)
        if crop_and_enlarge or invert:
            image_filepaths = preprocess(filepath, crop_and_enlarge=crop_and_enlarge, invert=invert)
        else:
            image_filepaths = [filepath]

        for image_filepath in image_filepaths:
            if not Path(image_filepath).is_file():
                print(f'Error: {Path(image_filepath).as_posix()} was not found or is not a file.')
                return None

            image = load_image(image_filepath)

            if SAM_model.lower() in {'fastsam', 'fast', 'f'}:
                directory = os.path.dirname(NPSAM.__file__)
                if not os.path.exists(os.path.join(directory, 'FastSAM.pt')):
                    print('The FastSAM weights will be downloaded:')
                    download_weights('FastSAM')
                start = time()
                fast_sam = FastSAM(os.path.join(directory, 'FastSAM.pt'))

                results = fast_sam(
                    source=image,
                    device=device,
                    retina_masks=True,
                    imgsz=image.shape[0],
                    conf=0.2,
                    iou=0.9,
                    verbose=False)

                prompt_process = FastSAMPrompt(image, results, device=device)

                masks = prompt_process.everything_prompt().cpu().numpy().transpose(1, 2, 0)

                list_of_masks = [masks[:, :, i] for i in range(masks.shape[2]) if masks[:, :, i][:, 0].sum() +
                                 masks[:, :, i][:, -1].sum() + masks[:, :, i][0, :].sum() + masks[:, :, i][-1,
                                                                                            :].sum() == 0]

            else:
                try:
                    sam_checkpoint, model_type = choose_SAM_model(SAM_model)
                except TypeError:
                    return print('Cannot run SAM because no weights are available.')
                start = time()

                # set up model
                sam = sam_model_registry[model_type](checkpoint=sam_checkpoint).to(device=device)

                mask_generator = SamAutomaticMaskGenerator(sam, points_per_side=PPS,
                                                           min_mask_region_area=min_mask_region_area, **kwargs)

                masks = mask_generator.generate(image)

                list_of_masks = [mask['segmentation'] for mask in masks if mask['segmentation'][:, 0].sum() +
                                 mask['segmentation'][:, -1].sum() + mask['segmentation'][0, :].sum() +
                                 mask['segmentation'][-1, :].sum() == 0]

            if prefilter:
                list_of_filtered_masks = []
                for i in range(len(list_of_masks)):
                    labels_of_masks = skimage.measure.label(list_of_masks[i])
                    props = skimage.measure.regionprops_table(labels_of_masks, properties=['label', 'area', 'solidity'])
                    if len(props.get('label')) == 1 and (props.get('area') < 400 or props.get('solidity') > 0.95):
                        list_of_filtered_masks.append(list_of_masks[i])
                list_of_masks = list_of_filtered_masks

            if len(list_of_masks) == 0:
                elapsed_time = time() - start
                print(
                    f'{len(list_of_masks)} masks found for {Path(image_filepath).name}, so no masks were saved.\nIt took {format_time(elapsed_time)}')
            else:
                array_of_masks = np.stack(list_of_masks, axis=-1)
                file_p = files_folder / (Path(image_filepath).stem + '_array_of_masks.npz')
                np.savez_compressed(file_p, array=array_of_masks)
                elapsed_time = time() - start
                print(f'{len(list_of_masks)} masks found. It took {format_time(elapsed_time)}')

        if crop_and_enlarge:
            stitch_crops_together(filepath, image_filepaths)
        else:
            if invert:
                file_p = files_folder / (Path(image_filepath).stem + '_array_of_masks.npz')
                if (files_folder / (Path(filepath).stem + '_array_of_masks.npz')).is_file():
                    (files_folder / (Path(filepath).stem + '_array_of_masks.npz')).unlink()
                file_p.rename(files_folder / (Path(filepath).stem + '_array_of_masks.npz'))


@overload(np.all)
def np_all(x, axis=None):
    # ndarray.all with axis arguments for 2D arrays.
    @register_jitable
    def _np_all_axis0(arr):
        out = np.logical_and(arr[0], arr[1])
        for v in iter(arr[2:]):
            for idx, v_2 in enumerate(v):
                out[idx] = np.logical_and(v_2, out[idx])
        return out

    @register_jitable
    def _np_all_axis1(arr):
        out = np.logical_and(arr[:, 0], arr[:, 1])
        for idx, v in enumerate(arr[:, 2:]):
            for v_2 in iter(v):
                out[idx] = np.logical_and(v_2, out[idx])
        return out

    def _np_all_impl(x, axis=None):
        if axis == 0:
            return _np_all_axis0(x)
        else:
            return _np_all_axis1(x)

    return _np_all_impl


@nb.njit(cache=True)
def nb_unique_caller(input_data):
    '''Numba compatible solution to numpy.unique() function'''

    data = input_data.copy()

    for i in range(data.shape[1] - 1, -1, -1):
        sorter = data[:, i].argsort(kind="mergesort")
        # mergesort to keep associations
        data = data[sorter]

    idx = [0]

    bool_idx = ~np.all((data[:-1] == data[1:]), axis=1)
    additional_uniques = np.nonzero(bool_idx)[0] + 1

    idx = np.append(idx, additional_uniques)

    return data[idx]


def import_segmentation(filepath, seg_filepath=None):
    filepaths = process_filepath(filepath)
    if seg_filepath:
        seg_filepaths = process_filepath(seg_filepath)

    for n, filepath in enumerate(filepaths):
        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')
        file_p = files_folder / (Path(filepath).stem + '_array_of_masks.npz')
        if file_p.is_file():
            overwrite = input(
                f'Importing another segmentation will delete {file_p.name} (which is produced when running SAM()). Continue (y/n)?')
            if overwrite == 'y':
                file_p.unlink()
            else:
                print('import_segmentation() was interupted.')
                return None
        if seg_filepath:
            segmentation = load_image(seg_filepaths[n])
        else:
            print(f'Please select the segmentation image for {Path(filepath).name} in the dialogue window.', end=' ')
            app = QApplication(sys.argv)
            fname = QFileDialog.getOpenFileName(None, f'Select the segmentation image for {Path(filepath).name}...',
                                                './',
                                                filter="Image files (*.png *.jpg *.jpeg *.tif *.tiff);;All files (*)")
            segmentation = load_image(fname[0])
        segmentation = segmentation[:, :, 0] > 0
        labels = label(segmentation)
        array_of_masks = np.dstack([labels == n for n in range(1, labels.max() + 1)])
        file_p = files_folder / (Path(filepath).stem + '_array_of_masks.npz')
        np.savez_compressed(file_p, array=array_of_masks)
        print('Import completed.')


def mask_plot(filepath, label_cmap='default', figsize=[8, 4]):
    if label_cmap == 'default':
        label_cmap = make_randomized_cmap()

    filepaths = process_filepath(filepath)

    for filepath in filepaths:
        if not Path(filepath).is_file():
            print(f'Error: {Path(filepath).as_posix()} was not found or is not a file.')
            return None

        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')

        file_p = files_folder / (Path(filepath).stem + '_array_of_masks.npz')
        masks = np.load(file_p)['array']
        masks = np.moveaxis(masks, -1, 0)
        weighted_masks = (masks * np.arange(1, masks.shape[0] + 1)[:, np.newaxis, np.newaxis])

        labels = np.zeros(weighted_masks[0].shape)
        for n in range(len(weighted_masks)):
            labels += weighted_masks[n]

        img = load_image(filepath)
        fig, ax = plt.subplots(1, 2, figsize=figsize)
        ax[0].imshow(img, cmap='gray')
        ax[0].axis('off')

        ax[1].imshow(labels, cmap=label_cmap, interpolation='nearest')
        ax[1].axis('off')

        plt.suptitle(Path(filepath).name)
        plt.tight_layout()
        plt.show()


def properties(filepath, scaling=True, stepsize=1):
    filepaths = process_filepath(filepath)

    scalings = []
    if type(scaling) == bool:
        if scaling:
            if len(filepaths) > 1:
                ask_for_common_scaling = input(f'Is the scaling for all the images? (y/n):')
            elif len(filepaths) == 1:
                ask_for_common_scaling = 'n'
            else:
                print('Error: no filepaths in filepath.')
                return None

            if ask_for_common_scaling == 'y':
                scalings = len(filepaths) * [float(input(f'Insert the scaling for the images in pixel pr nm:'))]
            elif ask_for_common_scaling == 'n':
                for filepath in filepaths:
                    scalings.append(float(input(f'Insert the scaling for {Path(filepath).name} in pixel pr nm:')))
            else:
                print('Invalid input. Try again.')
                return None

    elif type(scaling) == list:
        if len(scaling) == len(filepaths):
            scalings = [float(scale_factor) for scale_factor in scaling]
        else:
            print('Error: The length of the scaling list is not equal to the number of images.')
            return None

    elif type(scaling) in {int, float}:
        if len(filepaths) > 1:
            scalings = len(filepaths) * [float(scaling)]
        elif len(filepaths) == 1:
            scalings = [float(scaling)]
        else:
            print('Error: No filepaths in filepath.')

    if scaling:
        print('The following scalings will be used for the given images:')
        for (scale_factor, filepath) in zip(scalings, filepaths):
            print(f'{scale_factor} pixel pr nm for {Path(filepath).name}')

    for n, filepath in enumerate(filepaths):
        start = time()
        if not Path(filepath).is_file():
            print(f'Error: {Path(filepath).as_posix()} was not found or is not a file.')
            return None

        image = load_image(filepath)

        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')

        file_p = files_folder / (Path(filepath).stem + '_array_of_masks.npz')
        masks = np.load(file_p)['array']

        print(f'Finding mask properties in {Path(filepath).name}:')
        dfs_properties = []
        for m, mask in enumerate(np.moveaxis(masks, -1, 0)):
            print(f'Mask {m + 1}/{masks.shape[-1]}', sep=',',
                  end='\r' if m + 1 < masks.shape[-1] else '\n', flush=True)
            dfs_properties.append(pd.DataFrame(regionprops_table(mask.astype('uint8'), image[:, :, 0], properties=
            ('area', 'area_convex', 'axis_major_length', 'axis_minor_length', 'bbox', 'centroid', 'centroid_local',
             'centroid_weighted', 'coords', 'eccentricity', 'equivalent_diameter_area', 'euler_number', 'extent',
             'feret_diameter_max', 'inertia_tensor', 'inertia_tensor_eigvals', 'intensity_max', 'intensity_mean',
             'intensity_min', 'moments_hu', 'moments_weighted_hu', 'orientation', 'perimeter',
             'perimeter_crofton', 'solidity'))))
        df = pd.concat(dfs_properties)
        df['mask'] = np.arange(df.shape[0])
        df['mask_index'] = np.arange(df.shape[0])
        column_to_move = df.pop("mask_index")
        df.insert(0, "mask_index", column_to_move)
        df = df.set_index('mask')

        if scaling:
            pix_pr_nm = scalings[n]
            nm_pr_px = 1 / pix_pr_nm
            df['num_pixels'] = df['area'].astype(int)
            for property in ['equivalent_diameter_area', 'feret_diameter_max',
                             'perimeter', 'perimeter_crofton']:
                df[property] *= nm_pr_px
            for property in ['area', 'area_convex']:
                df[property] *= nm_pr_px ** 2
            df['scaling [pix/nm]'] = pix_pr_nm
        else:
            df['scaling [pix/nm]'] = 1

        df = df.round({
            'area': 1, 'area_convex': 1, 'axis_major_length': 1,
            'axis_minor_length': 1, 'centroid-0': 1, 'centroid-1': 1,
            'centroid_local-0': 1, 'centroid_local-1': 1,
            'centroid_weighted-0': 1, 'centroid_weighted-1': 1, 'eccentricity': 3,
            'equivalent_diameter_area': 1, 'extent': 3, 'feret_diameter_max': 1,
            'inertia_tensor-0-0': 1, 'inertia_tensor-0-1': 1,
            'inertia_tensor-1-0': 1, 'inertia_tensor-1-1': 1,
            'inertia_tensor_eigvals-0': 1, 'inertia_tensor_eigvals-1': 1,
            'intensity_max': 1, 'intensity_mean': 1, 'intensity_min': 1,
            'moments_hu-0': 3, 'moments_hu-1': 3, 'moments_hu-2': 3,
            'moments_hu-3': 3, 'moments_hu-4': 3, 'moments_hu-5': 3,
            'moments_hu-6': 3, 'moments_weighted_hu-0': 3,
            'moments_weighted_hu-1': 3, 'moments_weighted_hu-2': 3,
            'moments_weighted_hu-3': 3, 'moments_weighted_hu-4': 3,
            'moments_weighted_hu-5': 3, 'moments_weighted_hu-6': 3,
            'orientation': 3, 'perimeter': 1, 'perimeter_crofton': 1,
            'solidity': 3})

        print('Detecting areas with overlap.', end=' ')
        flattened_multiple_masks = masks[masks.sum(axis=-1) > 1]
        unique_multiple_masks = nb_unique_caller(flattened_multiple_masks[::stepsize])
        print('Done.')

        print('Processing areas with overlap:')
        df['overlap'] = 0
        df['overlapping_masks'] = [{n} for n in df.index.to_list()]
        for n, unique in enumerate(unique_multiple_masks):
            print(f'Area {n + 1}/{len(unique_multiple_masks)}', sep=',',
                  end='\r' if n + 1 < len(unique_multiple_masks) else '\n', flush=True)
            mask_indices = np.where(unique)[0]
            for overlapping_masks in df.loc[mask_indices]['overlapping_masks']:
                for mask_index in mask_indices:
                    overlapping_masks.add(mask_index)
            summed_masks = masks[:, :, mask_indices].sum(axis=-1)
            if summed_masks.max() > 1:
                overlap = (summed_masks == summed_masks.max()).sum()
            else:
                overlap = 0
            try:
                df.loc[mask_indices, 'overlap'] += overlap
            except KeyError:
                pass

        df['number_of_overlapping_masks'] = [len(masks) - 1 for masks in df['overlapping_masks'].to_list()]

        file_p = files_folder / (Path(filepath).stem + '_raw_dataframe.csv')
        df.to_csv(file_p, encoding='utf-8', header='true', index=False)
        elapsed_time = time() - start
        print(f'Done. It took {format_time(elapsed_time)}.')


def save_dictionary(filepath, dict):
    with open(filepath, "w") as fp:
        json.dump(dict, fp)


def load_dictionary(filepath):
    if Path(filepath).is_file():
        with open(filepath, "r") as fp:
            dict = json.load(fp)
        return dict
    else:
        return None


class ImageFilter:
    def __init__(self, filepath, image_number=1, label_cmap='default'):
        if label_cmap == 'default':
            self.label_cmap = make_randomized_cmap()
        else:
            self.label_cmap = label_cmap

        self.image_number = image_number
        self.filepaths = process_filepath(filepath)

        self.labels = None
        self.vmax = None
        self.image = None
        self.fig = None
        self.ax = None
        self.textvar = None
        self.filtered_label_image = None

        self.min_area = None
        self.max_area = None
        self.min_solidity = None
        self.max_solidity = None
        self.min_intensity = None
        self.max_intensity = None
        self.min_eccentricity = None
        self.max_eccentricity = None
        self.max_overlap = None
        self.overlapping_masks = None
        self.overlapping_masks_dict = {'All': "Not applied", '0': 0, '1': 1, '2': 2}

        self.ax_slider_area = None
        self.unit = None
        self.ax_slider_solidity = None
        self.ax_slider_intensity = None
        self.ax_slider_eccentricity = None
        self.ax_slider_overlap = None
        self.ax_radio_overlapping_masks = None
        self.ax_save = None
        self.ax_next = None
        self.ax_previous = None

    def get_df_params(self):
        return ((self.df['area'] >= self.min_area) & (self.df['area'] <= self.max_area) &
                (self.df['solidity'] >= self.min_solidity) & (self.df['solidity'] <= self.max_solidity) &
                (self.df['intensity_mean'] >= self.min_intensity) & (self.df['intensity_mean'] <= self.max_intensity) &
                (self.df['eccentricity'] >= self.min_eccentricity) & (
                            self.df['eccentricity'] <= self.max_eccentricity) &
                (self.df['number_of_overlapping_masks'] == self.overlapping_masks if type(self.overlapping_masks) == int
                 else self.df['number_of_overlapping_masks'] >= 0) & (self.df['overlap'] <= self.max_overlap))

    def plot_df(self, df):
        self.filtered_label_image = np.zeros(self.weighted_masks_rebinned[0].shape)
        for n in df.index.to_list():
            self.filtered_label_image += self.weighted_masks_rebinned[n]
        self.ax['left2'].clear()
        self.ax['left2'].imshow(self.filtered_label_image, cmap=self.label_cmap, interpolation='nearest', vmin=0,
                                vmax=self.vmax)
        self.ax['left2'].axis('off')

    def update_area(self, slider_area):
        self.min_area = int(slider_area[0])
        self.max_area = int(slider_area[1])

        self.area_val_text.set_text(f"Area {self.unit}: ({self.min_area}, {self.max_area})")

        df_area = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_area.shape[0]} labels removed.'
                                                  f' {df_area.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')
        self.plot_df(df_area)

    def update_solidity(self, slider_solidity):
        self.min_solidity = float(slider_solidity[0])
        self.max_solidity = float(slider_solidity[1])

        self.solidity_val_text.set_text(f"Solidity: ({self.min_solidity:.2f}, {self.max_solidity:.2f})")

        df_solidity = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_solidity.shape[0]} labels removed.'
                                                  f' {df_solidity.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')
        self.plot_df(df_solidity)

    def update_intensity(self, slider_intensity):
        self.min_intensity = int(slider_intensity[0])
        self.max_intensity = int(slider_intensity[1])

        self.intensity_val_text.set_text(f"Intensity: ({self.min_intensity}, {self.max_intensity})")

        df_intensity = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_intensity.shape[0]} labels removed.'
                                                  f' {df_intensity.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')
        self.plot_df(df_intensity)

    def update_eccentricity(self, slider_eccentricity):
        self.min_eccentricity = float(slider_eccentricity[0])
        self.max_eccentricity = float(slider_eccentricity[1])

        self.eccentricity_val_text.set_text(f"Eccentricity: ({self.min_eccentricity:.2f}, {self.max_eccentricity:.2f})")

        df_eccentricity = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_eccentricity.shape[0]} labels removed.'
                                                  f' {df_eccentricity.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')

        self.plot_df(df_eccentricity)

    def update_overlap(self, slider_overlap):
        self.max_overlap = slider_overlap

        self.overlap_val_text.set_text(f"Overlap: {self.max_overlap}")

        df_overlap = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_overlap.shape[0]} labels removed.'
                                                  f' {df_overlap.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')

        self.plot_df(df_overlap)

    def update_overlapping_masks(self, label):
        self.overlapping_masks = self.overlapping_masks_dict[label]

        df_overlapping_masks = self.df.loc[self.get_df_params()]

        self.textvar.remove()
        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0] - df_overlapping_masks.shape[0]} labels removed.'
                                                  f' {df_overlapping_masks.shape[0]} remain.', fontsize=16,
                                     horizontalalignment='center', verticalalignment='center')

        self.plot_df(df_overlapping_masks)

        self.fig.canvas.draw()
        
    def on_pick(self, event):
        if event.inaxes == self.ax['left2']:
            x, y = int(event.xdata), int(event.ydata)
            print(x,y)
            print(event.button, event.x, event.xdata, event.y, event.ydata)


    def update_button(self):
        df_filtered = self.df.loc[self.get_df_params()]
        self.plot_df(df_filtered)

        filters = {
            'min_area': self.min_area,
            'max_area': self.max_area,
            'min_solidity': self.min_solidity,
            'max_solidity': self.max_solidity,
            'min_intensity': self.min_intensity,
            'max_intensity': self.max_intensity,
            'min_eccentricity': self.min_eccentricity,
            'max_eccentricity': self.max_eccentricity,
            'scaling': self.df['scaling [pix/nm]'].to_list()[1],
            'overlap': self.max_overlap,
            'overlapping_masks': self.overlapping_masks,
            'removed': self.df.shape[0] - df_filtered.shape[0],
            'remain': df_filtered.shape[0]
        }

        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filtered_dataframe.csv')
        df_filtered.to_csv(self.file_p, encoding='utf-8', header='true', index=False)
        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filters_dict.txt')
        save_dictionary(self.file_p, filters)

        self.filtered_label_image = np.zeros(self.weighted_masks[0].shape)
        for n in df_filtered.index.to_list():
            self.filtered_label_image += self.weighted_masks[n]
        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filtered_masks.png')
        plt.imsave(self.file_p, self.filtered_label_image, cmap=self.label_cmap)
        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filtered_masks.tif')
        tifffile.imwrite(self.file_p, self.filtered_label_image.astype('uint16'))
        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filtered_binary_labels.tif')
        tifffile.imwrite(self.file_p, ((self.filtered_label_image > 0) * 255).astype('uint8'))

        plt.close()

    def final_save(self, save_button):
        self.update_button()

    def update_next(self, next_button):
        self.update_button()

        self.image_number += 1

        self.filter()

    def update_previous(self, previous_button):
        self.update_button()

        self.image_number -= 1

        self.filter()

    def create_area_slider(self, ax, df):
        self.unit = "$(nm^2)$" if self.df['scaling [pix/nm]'].to_list()[0] != 1 else "$(px)$"

        self.slider_area = RangeSlider(ax, '', valmin=self.min_area, valmax=self.max_area, valstep=1,
                                       valinit=(self.min_area_init, self.max_area_init))
        self.slider_area.on_changed(self.update_area)

        self.area_val_text = ax.text(0, 1.12, f"Area {self.unit}: ({self.min_area}, {self.max_area})",
                                     fontsize=14, ha='left', va='center', transform=ax.transAxes)
        self.slider_area.valtext.set_visible(False)
        self.update_area((self.min_area_init, self.max_area_init))

    def create_solidity_slider(self, ax):
        self.slider_solidity = RangeSlider(ax, "", valmin=self.min_solidity, valmax=1, valstep=0.001,
                                           valinit=(self.min_solidity_init, self.max_solidity_init))
        self.slider_solidity.on_changed(self.update_solidity)

        self.solidity_val_text = ax.text(0, 1.12, f"Solidity: ({self.min_solidity}, {self.max_solidity})",
                                         fontsize=14, ha='left', va='center', transform=ax.transAxes)
        self.slider_solidity.valtext.set_visible(False)
        self.update_solidity((self.min_solidity_init, self.max_solidity_init))

    def create_intensity_slider(self, ax):
        self.slider_intensity = RangeSlider(ax, "", valmin=self.min_intensity, valmax=self.max_intensity,
                                            valstep=1, valinit=(self.min_intensity_init, self.max_intensity_init))
        self.slider_intensity.on_changed(self.update_intensity)

        self.intensity_val_text = ax.text(0, 1.12, f"Intensity: ({self.min_intensity}, {self.max_intensity})",
                                          fontsize=14, ha='left', va='center', transform=ax.transAxes)
        self.slider_intensity.valtext.set_visible(False)
        self.update_intensity((self.min_intensity_init, self.max_intensity_init))

    def create_eccentricity_slider(self, ax):
        self.slider_eccentricity = RangeSlider(ax, "", valmin=0, valmax=1, valstep=0.01,
                                               valinit=(self.min_eccentricity_init, self.max_eccentricity_init))
        self.slider_eccentricity.on_changed(self.update_eccentricity)

        self.eccentricity_val_text = ax.text(0, 1.12,
                                             f"Eccentricity: ({self.min_eccentricity}, {self.max_eccentricity})",
                                             fontsize=14, ha='left', va='center', transform=ax.transAxes)
        self.slider_eccentricity.valtext.set_visible(False)
        self.update_eccentricity((self.min_eccentricity_init, self.max_eccentricity_init))

    def create_overlap_slider(self, ax):
        self.slider_overlap = Slider(ax, '', valmin=0, valmax=self.max_overlap, valstep=1,
                                     valinit=self.max_overlap_init)
        self.slider_overlap.on_changed(self.update_overlap)

        self.overlap_val_text = ax.text(0, 1.12, f"Overlap: {self.max_overlap}",
                                        fontsize=14, ha='left', va='center', transform=ax.transAxes)
        self.slider_overlap.valtext.set_visible(False)
        self.slider_overlap.vline._linewidth = 0
        self.update_overlap(self.max_overlap_init)

    def create_overlapping_masks_radio(self, ax):
        ax.set_aspect('equal')
        if type(self.overlapping_masks_init) == str:
            self.overlapping_masks_init = -1
        elif self.overlapping_masks_init > 2:
            self.overlapping_masks_init = -1
        self.radio_overlapping_masks = RadioButtons(ax, ('All', '0', '1', '2'),
                                                    active=self.overlapping_masks_init + 1, activecolor='#1F77B4')

        dists = [0, 0.12, 0.235, 0.35]
        for i, (circle, label) in enumerate(
                zip(self.radio_overlapping_masks.circles, self.radio_overlapping_masks.labels)):
            new_x = 0.6 + dists[i]
            new_y = 0.5
            circle.set_center((new_x, new_y))
            circle.set_radius(0.02)
            label.set_position((new_x + 0.03, new_y))
            label.set_fontsize(14)

        self.overlapping_masks_val_text = ax.text(0, 0.5, "Number of overlapping masks:",
                                                  fontsize=14, ha='left', va='center', transform=ax.transAxes)

        self.radio_overlapping_masks.on_clicked(self.update_overlapping_masks)
        self.update_overlapping_masks(['All', '0', '1', '2'][self.overlapping_masks_init + 1])

    def create_save_button(self, ax):
        self.save_button = Button(ax, 'Save and\nclose', color='#A2CD56', hovercolor='#79B356')
        self.save_button.label.set_fontsize(18)
        self.save_button.on_clicked(self.final_save)

    def create_next_button(self, ax):
        self.next_button = Button(ax, 'Next', color='#A2CD56', hovercolor='#79B356')
        self.next_button.label.set_fontsize(18)
        self.next_button.on_clicked(self.update_next)

    def create_previous_button(self, ax):
        self.previous_button = Button(ax, 'Previous', color='#F0B54A', hovercolor='#DC9834')
        self.previous_button.label.set_fontsize(18)
        self.previous_button.on_clicked(self.update_previous)

    def initiate_filter_values(self):
        if self.filters_init:
            self.min_area_init = self.filters_init['min_area']
            self.max_area_init = self.filters_init['max_area']
            self.min_solidity_init = self.filters_init['min_solidity']
            self.max_solidity_init = self.filters_init['max_solidity']
            self.min_intensity_init = self.filters_init['min_intensity']
            self.max_intensity_init = self.filters_init['max_intensity']
            self.min_eccentricity_init = self.filters_init['min_eccentricity']
            self.max_eccentricity_init = self.filters_init['max_eccentricity']
            self.max_overlap_init = self.filters_init['overlap']
            self.overlapping_masks_init = self.filters_init['overlapping_masks']
        else:
            self.min_area_init = self.min_area
            self.max_area_init = self.max_area
            self.min_solidity_init = self.min_solidity
            self.max_solidity_init = self.max_solidity
            self.min_intensity_init = self.min_intensity
            self.max_intensity_init = self.max_intensity
            self.min_eccentricity_init = self.min_eccentricity
            self.max_eccentricity_init = self.max_eccentricity
            self.max_overlap_init = self.max_overlap
            self.overlapping_masks_init = self.overlapping_masks



    def start_plot(self, image, labels):
        self.fig, self.ax = plt.subplot_mosaic([['left', 'right'], ['left2', 'right2']],
                                               constrained_layout=True, figsize=(12, 9))

        
        self.ax['left'].imshow(image, cmap='gray')
        self.vmax = labels.max()
        self.ax['right'].imshow(labels, cmap=self.label_cmap, interpolation='nearest', vmin=0, vmax=self.vmax)
        self.ax['left2'].imshow(self.filtered_masks_rebinned, cmap=self.label_cmap, interpolation='nearest', vmin=0, vmax=self.vmax)

        for axis in self.ax:
            self.ax[axis].axis('off')
            
        self.ax_radio_overlapping_masks = plt.axes([0.5, -0.12, 0.5, 0.6], frameon=False)
        self.ax_slider_area = plt.axes([0.525, 0.430, 0.45, 0.03], facecolor='teal')
        self.ax_slider_solidity = plt.axes([0.525, 0.375, 0.45, 0.03], facecolor='teal')
        self.ax_slider_intensity = plt.axes([0.525, 0.320, 0.45, 0.03], facecolor='teal')
        self.ax_slider_eccentricity = plt.axes([0.525, 0.265, 0.45, 0.03], facecolor='teal')
        self.ax_slider_overlap = plt.axes([0.525, 0.210, 0.45, 0.03], facecolor='teal')

        self.ax_save = plt.axes([0.835, 0.01, 0.14, 0.085])
        self.create_save_button(self.ax_save)
        if self.image_number < len(self.filepaths):
            self.ax_next = plt.axes([0.68, 0.01, 0.14, 0.085])
            self.create_next_button(self.ax_next)
        if self.image_number != 1:
            self.ax_previous = plt.axes([0.525, 0.01, 0.14, 0.085])
            self.create_previous_button(self.ax_previous)

        self.min_area = math.floor(self.df['area'].min())
        self.max_area = math.ceil(self.df['area'].max())

        self.min_intensity = math.floor(self.df['intensity_mean'].min())
        self.max_intensity = math.ceil(self.df['intensity_mean'].max())

        self.max_overlap = math.ceil(self.df['overlap'].max())

        self.textvar = self.fig.text(0.704, 0.12, f'{self.df.shape[0]} labels found.',
                                     horizontalalignment='center', verticalalignment='center', fontsize=16)

        self.min_solidity = self.df['solidity'].min()
        self.max_solidity = 1

        self.min_eccentricity = 0
        self.max_eccentricity = 1

        self.overlapping_masks = "Not applied"

        self.initiate_filter_values()

        self.create_area_slider(self.ax_slider_area, self.df)
        self.create_solidity_slider(self.ax_slider_solidity)
        self.create_intensity_slider(self.ax_slider_intensity)
        self.create_eccentricity_slider(self.ax_slider_eccentricity)
        self.create_overlap_slider(self.ax_slider_overlap)
        self.create_overlapping_masks_radio(self.ax_radio_overlapping_masks)
        self.fig.canvas.mpl_connect('button_press_event', self.on_pick)



        string_title = f'Image number {self.image_number} out of {len(self.filepaths)} - {Path(self.filepath).name}'

        plt.suptitle(string_title, fontsize=16)

        plt.show()

    def filter(self):
        self.filepath = self.filepaths[self.image_number - 1]
        self.files_folder = Path(self.filepath).parent / (Path(self.filepath).stem + '_files')
        self.file_p = self.files_folder / (Path(self.filepath).stem + '_raw_dataframe.csv')
        self.df = pd.read_csv(self.file_p)

        self.file_p = self.files_folder / (Path(self.filepath).stem + '_array_of_masks.npz')
        self.masks = np.load(self.file_p)['array']
        self.masks = np.moveaxis(self.masks, -1, 0)
        self.weighted_masks = (self.masks * np.arange(1, self.masks.shape[0] + 1)[:, np.newaxis, np.newaxis])
        self.weighted_masks_rebinned = self.weighted_masks[:, ::4, ::4]

        self.labels = np.zeros(self.weighted_masks[0].shape)
        for n in self.df.index.to_list():
            self.labels += self.weighted_masks[n]

        self.filtered_masks_rebinned = np.zeros(self.weighted_masks_rebinned[0].shape)
        for n in self.df.index.to_list():
            self.filtered_masks_rebinned += self.weighted_masks_rebinned[n]

        self.image = load_image(self.filepath)

        self.file_p = self.files_folder / (Path(self.filepath).stem + '_filters_dict.txt')
        self.filters_init = load_dictionary(self.file_p)

        self.start_plot(self.image, self.labels)


def manual_filter(filepath, conditions, label_cmap='default'):
    if label_cmap == 'default':
        label_cmap = make_randomized_cmap()
    filepaths = process_filepath(filepath)

    if type(conditions) == dict:
        conditions = [conditions] * len(filepaths)
        if len(filepaths) > 1:
            print('The filtering conditions will be used for all images.')
    elif type(conditions) == list:
        if len(conditions) == len(filepaths):
            for entry in conditions:
                if type(entry) != dict:
                    print('The list entries must be dictionaries containing the filter conditions.')
                    return None
        elif len(conditions) == 1:
            conditions = conditions * len(filepaths)
            print('The filtering conditions will be used for all images.')
        else:
            print(
                'The length of the list with filtering conditions does not have the same length as the list with image filepaths.')
            return None

    for filter_conditions, filepath in zip(conditions, filepaths):
        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')
        file_p = files_folder / (Path(filepath).stem + '_raw_dataframe.csv')
        df = pd.read_csv(file_p)

        file_p = files_folder / (Path(filepath).stem + '_array_of_masks.npz')
        masks = np.load(file_p)['array']
        masks = np.moveaxis(masks, -1, 0)
        weighted_masks = (masks * np.arange(1, masks.shape[0] + 1)[:, np.newaxis, np.newaxis])

        filters = {'min_area': math.floor(df['area'].min()),
                   'max_area': math.ceil(df['area'].max()),
                   'min_solidity': 0,
                   'max_solidity': 1,
                   'min_intensity': math.floor(df['intensity_mean'].min()),
                   'max_intensity': math.ceil(df['intensity_mean'].max()),
                   'min_eccentricity': 0,
                   'max_eccentricity': 1,
                   'overlap': math.ceil(df['overlap'].max()),
                   'overlapping_masks': "Not applied",
                   'scaling': df['scaling [pix/nm]'].to_list()[1]}

        filters.update(filter_conditions)

        filtered_df = df[((df['area'] >= filters['min_area']) & (df['area'] <= filters['max_area']) &
                          (df['solidity'] >= filters['min_solidity']) & (df['solidity'] <= filters['max_solidity']) &
                          (df['intensity_mean'] >= filters['min_intensity']) & (
                                      df['intensity_mean'] <= filters['max_intensity']) &
                          (df['eccentricity'] >= filters['min_eccentricity']) & (
                                      df['eccentricity'] <= filters['max_eccentricity']) &
                          (df['number_of_overlapping_masks'] == filters['overlapping_masks'] if type(
                              filters['overlapping_masks']) == int
                           else df['number_of_overlapping_masks'] >= 0) & (df['overlap'] <= filters['overlap']))]

        filters.update({'removed': df.shape[0] - filtered_df.shape[0], 'remain': filtered_df.shape[0]})

        filtered_label_image = np.zeros(weighted_masks[0].shape)
        for n in filtered_df.index.to_list():
            filtered_label_image += weighted_masks[n]

        file_p = files_folder / (Path(filepath).stem + '_filtered_dataframe.csv')
        filtered_df.to_csv(file_p, encoding='utf-8', header='true', index=False)
        file_p = files_folder / (Path(filepath).stem + '_filters_dict.txt')
        save_dictionary(file_p, filters)
        file_p = files_folder / (Path(filepath).stem + '_filtered_masks.png')
        plt.imsave(file_p, filtered_label_image, cmap=label_cmap)
        file_p = files_folder / (Path(filepath).stem + '_filtered_masks.tif')
        tifffile.imwrite(file_p, filtered_label_image.astype('uint16'))
        file_p = files_folder / (Path(filepath).stem + '_filtered_binary_labels.tif')
        tifffile.imwrite(file_p, ((filtered_label_image > 0) * 255).astype('uint8'))


def overview(filepath, property_list=['area'], bin_list=None, timestamp=False):
    filepaths = process_filepath(filepath)

    for n, property in enumerate(property_list):
        if property == 'intensity':
            property_list[n] = 'intensity_mean'
        elif property == 'diameter':
            property_list[n] = 'equivalent_diameter_area'
        elif property == 'max diameter':
            property_list[n] = 'feret_diameter_max'
        elif property == 'crofton perimeter':
            property_list[n] = 'perimeter_crofton'
        elif property == 'convex area':
            property_list[n] = 'area_convex'

    dfs = []
    imagenumber = 1
    for filepath in filepaths:
        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')
        file_p = files_folder / (Path(filepath).stem + '_filtered_dataframe.csv')
        df_filtered = pd.read_csv(file_p)
        df_filtered['imagename'] = Path(filepath).name
        df_filtered['imagenumber'] = imagenumber
        imagenumber += 1
        dfs.append(df_filtered)
    master_df = pd.concat(dfs)
    file_p = Path(filepaths[0]).parent / 'NPSAM_overview_filtered_dataframe.csv'

    if bin_list == None:
        bin_list = [len(master_df) // 10] * len(property_list)

    first_column = master_df.pop('imagename')
    second_column = master_df.pop('imagenumber')
    master_df.insert(0, 'imagename', first_column)
    master_df.insert(1, 'imagenumber', second_column)
    master_df.to_csv(file_p, encoding='utf-8', header='true', index=False)
    if timestamp:
        d = datetime.now()
        stamp = str(d.year) + str(d.month) + str(d.day) + '-' + str(d.hour) + str(d.minute) + str(d.second)
        file_p = Path(filepaths[0]).parent / ('NPSAM_overview_' + stamp + '.pdf')
    else:
        file_p = Path(filepaths[0]).parent / 'NPSAM_overview.pdf'
    master_pp = PdfPages(file_p)

    unit = "$(nm)$" if master_df['scaling [pix/nm]'].to_list()[0] != 1 else "$(px)$"
    unit2 = "$(nm^2)$" if master_df['scaling [pix/nm]'].to_list()[0] != 1 else "$(px)$"
    name_dict = {'area': f'area {unit2}', 'area_convex': f'convex area {unit2}', 'eccentricity': 'eccentricity',
                 'solidity': 'solidity', 'intensity_mean': 'mean intensity', 'overlap': 'overlap (pix)',
                 'equivalent_diameter_area': f'area equivalent diameter {unit}',
                 'feret_diameter_max': f'Max diameter (Feret) {unit}', 'orientation': 'orientation',
                 'perimeter': f'perimeter {unit}', 'perimeter_crofton': f'crofton perimeter {unit}'}
    for n, prop in enumerate(property_list):
        fig, ax = plt.subplots(figsize=(12, 9))
        ax.set_xlabel(name_dict.get(prop).capitalize(), fontsize=16)
        ax.set_title(f'Histogram of {name_dict.get(prop)} for all images', fontsize=18)
        master_df[prop].hist(bins=bin_list[n], ax=ax)
        ax.grid(False)
        ax.set_ylabel('Count', fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=14)
        plt.show()
        master_pp.savefig(fig)

    for filepath in filepaths:
        img = load_image(filepath)
        files_folder = Path(filepath).parent / (Path(filepath).stem + '_files')
        file_p = files_folder / (Path(filepath).stem + '_filtered_dataframe.csv')
        df_filtered = pd.read_csv(file_p)
        file_p = files_folder / (Path(filepath).stem + '_filtered_masks.png')
        labels = load_image(file_p.as_posix())

        fig, ax = plt.subplot_mosaic([['left', 'right'], ['left2', 'right2']],
                                     constrained_layout=True, figsize=(12, 9))
        ax['left'].imshow(img, cmap='gray')
        ax['left'].axis('off')

        ax['right'].imshow(labels, interpolation='nearest')
        ax['right'].axis('off')

        ax['right2'].axis('off')

        plt.suptitle(Path(filepath).name)

        unit = "$(nm^2)$" if df_filtered['scaling [pix/nm]'][0] != 1 else "$(px)$"

        df_filtered['area'].hist(bins=10, ax=ax['left2'])
        ax['left2'].set_title(f'Histogram of area {unit}')
        ax['left2'].set_xlabel(f'area {unit}')
        ax['left2'].grid(False)
        ax['left2'].set_ylabel('Count')

        file_p = files_folder / (Path(filepath).stem + '_filters_dict.txt')
        filters = load_dictionary(file_p)
        min_area = filters['min_area']
        max_area = filters['max_area']
        min_solidity = filters['min_solidity']
        max_solidity = filters['max_solidity']
        min_intensity = filters['min_intensity']
        max_intensity = filters['max_intensity']
        min_eccentricity = filters['min_eccentricity']
        max_eccentricity = filters['max_eccentricity']
        overlap = filters['overlap']
        overlapping_masks = filters['overlapping_masks']
        scaling = filters['scaling']
        removed = filters['removed']
        remain = filters['remain']

        fig.text(0.5845, 0.455, 'Used parameter values:', fontsize=18, multialignment='center')

        fig.text(0.5845, 0.415, f'Area {unit}:             ({round(min_area, 1)},'
                                f' {round(max_area, 1)})', fontsize=18, multialignment='center')
        fig.text(0.5845, 0.375, f'Solidity:                   ({min_solidity}, {max_solidity})', fontsize=18,
                 multialignment='center')
        fig.text(0.5845, 0.335, f'Intensity:                 ({min_intensity}, {max_intensity})', fontsize=18,
                 multialignment='center')
        fig.text(0.5845, 0.295, f'Eccentricity:            ({min_eccentricity}, {max_eccentricity})', fontsize=18,
                 multialignment='center')
        fig.text(0.5845, 0.255, f'Overlap:                  {overlap}', fontsize=18, multialignment='center')
        fig.text(0.5845, 0.185, f'Number of \noverlapping masks: {overlapping_masks}', fontsize=18,
                 multialignment='left')
        fig.text(0.5845, 0.145, f'Scaling (pix/nm):     {scaling}', fontsize=18, multialignment='center')
        fig.text(0.63, 0.055, f'{removed} labels removed.\n {remain} remain.', fontsize=18, multialignment='center')

        plt.show()

        file_p = files_folder / (Path(filepath).stem + '_overview.pdf')
        pp = PdfPages(file_p)
        pp.savefig(fig)
        master_pp.savefig(fig)
        pp.close()

    master_pp.close()
