import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO(r'ultralytics\cfg\models\fre\fre-yolo\fre-yolo.yaml', task='detect') # select your model.yaml path
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset\data.yaml', # select your data.yaml path
                cache=False,
                imgsz=640,
                epochs=1000,
                batch=32,
                patience=500, 
                close_mosaic=10,
                workers=16,
                device='0',
                # optimizer='SGD', # using SGD 
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
