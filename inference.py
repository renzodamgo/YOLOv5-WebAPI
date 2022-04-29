import torch
from PIL import Image
import io


model = torch.hub.load(
        "ultralytics/yolov5", "custom", path='./best.pt', force_reload=True, autoshape=True
    )  # force_reload = recache latest code
model.eval()


def get_prediction(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    results = model(img, size=640)
    results.render()  # updates results.imgs with boxes and labels
    for img in results.imgs:
        img_base64 = Image.fromarray(img)
        img_base64.save("static/image0.jpg", format="JPEG")