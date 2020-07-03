# Seamless Scene Segmentation

This repository is forked from [Seamseg](https://github.com/mapillary/seamseg).

### Setup

Main system requirements:
* CUDA 10.1
* Linux with GCC 7 or 8
* PyTorch v1.1.0
```bash
pip install -r requirements.txt
cd seamseg
python setup.py develop
```

### Trained models

The model files provided below are made available under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.

| Model | PQ | Link + md5 |
|-------|----|------------|
| SeamSeg ResNet50, Mapillary Vistas | 37.99 | [7046e54e54e9dcc38060b150e97f4a5a][1] |

[1]: https://drive.google.com/file/d/1ULhd_CZ24L8FnI9lZ2H6Xuf03n6NA_-Y/view

The files linked above are `zip` archives, each containing model weights (`.tar` file), configuration parameters (`config.ini` file) and the metadata file of the dataset the model was trained on (`metadata.bin` file).
To use a model, unzip it somewhere and follow the instructions in the [Running inference"](#running-inference) section below.

### Running inference

Given a trained network, inference can be run on any set of images using
[scripts/test_panoptic.py](scripts/test_panoptic.py):

```bash
cd scripts
python -m torch.distributed.launch --nproc_per_node=N_GPUS test_panoptic.py --meta METADATA --log_dir LOG_DIR CONFIG MODEL INPUT_DIR OUTPUT_DIR
```
Images (either `png` or `jpg`) will be read from `INPUT_DIR` and recursively in all subfolders, and predictions will be
written to `OUTPUT_DIR`.
The script also requires to be given the `metadata.bin` file of the dataset the network was originally trained on.
Note that the script will only read from the `"meta"` section, meaning that a stripped-down version of `metadata.bin`,
i.e. without the `"images"` section, can also be used.

By default, the test scripts output "qualitative" results, i.e. the original images superimposed with their panoptic segmentation.
This can be changed by setting the `--raw` flag: in this case, the script will output, for each image, the "raw" network
output as a PyTorch `.pth.tar` file.
An additional script to process these raw outputs into COCO-format panoptic predictions will be released soon.

