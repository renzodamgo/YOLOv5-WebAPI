import torch
from PIL import Image
import io


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # force_reload = recache latest code
model.eval()
print("Model initialized")

def get_prediction(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    results = model(img, size=640)
    return results
