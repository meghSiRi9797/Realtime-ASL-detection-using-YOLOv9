from ultralytics import YOLO

model = YOLO('C:/Users/megha/Downloads/ASL/models/yolov9c.pt')  
model.export(format='torchscript')    # Export the model
