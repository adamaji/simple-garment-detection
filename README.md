## Simple garment detector
A simple proof of concept web app to show clothing detection on images

This app uses a detection model to find a small amount of clothing categories in images. The model is trained with the faster rcnn code from [maskrcnn-benchmark](https://github.com/ajiraffe/maskrcnn-benchmark/tree/simple_clothes) on a *small* dataset of street fashion images.

## Pretrained models

You can find the pretrained model [here](https://drive.google.com/open?id=1zkRkaxAuo1cXN_7Z8X3cJXWrZgwl7JTO) temporarily. Given the time constraint and because I didn't want to spend any money on gpu time, this was trained on Google Colab. I might add the notebook here later.

## Running

To run this locally, first copy the trained model weights file to the `models` directory and then do

```
export FLASK_APP=index.py
flask run
```

