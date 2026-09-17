"""
PROJECT: Detecting Traffic Signs With YOLOv8
METHOD(transfer-learning): Fine-tuning a pre-trained YOLOv8 model with a new dataset. Updating output layer's weights
 
STEPS:
1-İmport libraries
2-Find dataset
3-Load dataset
4-Training
5-Testing

"""
from ultralytics import YOLO
import torch
import torchvision
def main():
    model=YOLO("yolov8n.pt")
    model.train(
        data="traffic-sign-detector/data.yaml",#use data in data.yaml folder.
        epochs=10,#training iterations
        imgsz=640,#image size for incoming images
        batch=16,#batch_size
        name="traffic-sign-fourth-model",#final folder name
        lr0=0.01,#learning rate, learning speed
        optimizer="SGD",
        weight_decay=0.0005,#weight penalty
        momentum=0.935,#momentum rate for SGD
        patience=50,#stops training after 50 epochs without any changes.
        workers=2,#working gpu cores
        device="cuda",#model will be trained on gpu
        save=True,#save model 
        save_period=1,#save model after every epoch
        val=True,#apply validation after every epoch
        verbose=True#monitor detailed training process
    )
if __name__=="__main__":
    main()

