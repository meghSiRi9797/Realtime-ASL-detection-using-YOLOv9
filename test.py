from ultralytics import YOLO

model = YOLO('C:/Users/megha/Downloads/ASL/models/yolov9c.pt')  
#model.export(format='torchscript')    # Export the model
model.export(format='torchscript', imgsz=640)  # export to TorchScript
