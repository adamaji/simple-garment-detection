from PIL import Image
import requests
from io import BytesIO
import numpy as np
import base64

from maskrcnn_benchmark.config import cfg
from demo.simple_clothes_predictor import ClothesDemo

from flask import Flask, request, render_template, send_file
app = Flask(__name__)

# set up the predictor from maskrcnn-benchmark
config_file = "./maskrcnn-benchmark/configs/simple_clothes/e2e_faster-rcnn_inference.yaml"
cfg.merge_from_file(config_file)
cfg.merge_from_list(["MODEL.DEVICE", "cpu"])
predictor = ClothesDemo(
    cfg,
    min_image_size=800,
    confidence_threshold=0.7
)

# main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post_url():
    text = request.form['texturl']
    url = text
    try:
        response = requests.get(url)
        pil_image = Image.open(BytesIO(response.content)).convert("RGB")
        image = np.array(pil_image)[:, :, [2, 1, 0]]

        preds = get_predictions(image)
        print(len(preds))
        return render_template('results.html', images=preds)

    except Exception as e:
        return "Could not open image " + str(e)

    return render_template('index.html')

# return the original image and model predictions as byte strings
def get_predictions(image):
    predictions = predictor.run_on_opencv_image(image)

    image_pil = Image.fromarray(image[:, :, [2, 1, 0]])

    predictions_pil = Image.fromarray(predictions[:, :, [2, 1, 0]]
)

    byte_image = BytesIO()
    image_pil.save(byte_image, 'JPEG')
    byte_image.seek(0)

    byte_preds = BytesIO()
    predictions_pil.save(byte_preds, 'JPEG')
    byte_preds.seek(0)

    img = base64.b64encode(byte_image.getvalue())
    res = base64.b64encode(byte_preds.getvalue())

    return [img.decode('ascii'), res.decode('ascii')]

