# FRE-YOLOv8
This repository contains the code implementation for the experiments described in the paper "
FRE-YOLO: An Improved YOLOv8 Algorithm for Real Time Railway Damage Detection".

## Model
The project files is modified based on the [YOLOv8](https://github.com/ultralytics/ultralytics) project. The model configuration file [fre-yolo.yaml](https://github.com/haichao67/FRE-YOLO/blob/master/ultralytics/cfg/models/fre/fre-yolo/fre-yolo.yaml) is located in the directory [./ultralytics/cfg/models/fre/fre-yolo](https://github.com/haichao67/FRE-YOLO/tree/master/ultralytics/cfg/models/fre/fre-yolo).

### Recommended Configuration
- Python: 3.8
- Torch: 2.4.1
- Torchvision: 0.19.1

### Additional Packages Required
Install packages by yourself if they are not already installed
Recommended dependencies:
pip install timm==1.0.7 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.4.8 dill==0.3.8 albumentations==1.4.11 pytorch_wavelets==1.3.0 tidecv PyWavelets opencv-python

## Training
Run the [train.py](https://github.com/haichao67/FRE-YOLO/blob/master/train.py) file. The default hyperparameters are located in the [./ultralytics/cfg/default.yaml](https://github.com/haichao67/FRE-YOLO/blob/master/ultralytics/cfg/default.yaml) file.
**Note**: Please modify the model path and [data.yaml](https://github.com/haichao67/FRE-YOLO/blob/master/dataset/data.yaml) file path in [train.py](https://github.com/haichao67/FRE-YOLO/blob/master/train.py) as needed. The default location for [data.yaml](https://github.com/haichao67/FRE-YOLO/blob/master/dataset/data.yaml) is [./dataset](https://github.com/haichao67/FRE-YOLO/blob/master/dataset). The dataset format is the same as that used in the YOLOv8 project.
## Validation
Run the [val.py](https://github.com/haichao67/FRE-YOLO/blob/master/val.py) file to obtain precision, recall, and mAP, etc. Run the [get_FPS.py](https://github.com/haichao67/FRE-YOLO/blob/master/get_FPS.py) file to obtain FPS.The modification method is consistent with training.

## Inference on Images
Run the [detect.py](https://github.com/haichao67/FRE-YOLO/blob/master/detect.py) file. The modification method is consistent with training.

## Evaluation
We have trained and evaluated FRE-YOLO on the dataset, which is included in the project. The trained model weights file is located at [./weight/fre-yolo](https://github.com/haichao67/FRE-YOLO/tree/master/weight/fre-yolo).

## Ablation Experiments
For the ablation experiments described in the paper, the model weights files are located in the [./weight/ablation](https://github.com/haichao67/FRE-YOLO/tree/master/weight/ablation) folder.

## Copyright Notice
Many utility codes of our project are based on the codes from the [ultralytics](https://github.com/ultralytics/ultralytics) and [RCS-YOLO](https://github.com/mkang315/RCS-YOLO/tree/main) and [FocalNet](https://github.com/microsoft/FocalNet)
