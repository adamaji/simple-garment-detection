## Simple garment detector
A simple proof of concept web app to show clothing detection on images

This is a simple app which uses a detection model to find a small amount of clothing categories in images. The model is trained with slightly modified faster rcnn code from [maskrcnn-benchmark](https://github.com/adamaji/maskrcnn-benchmark/tree/simple_clothes) on a *small* dataset of street fashion images.

## Pretrained models

You can find the pretrained model [here](https://drive.google.com/open?id=1zkRkaxAuo1cXN_7Z8X3cJXWrZgwl7JTO) temporarily. Given the time constraint and because I didn't want to spend any money on gpu time, this was trained on Google Colab. The notebook I used to train is [here](./tools/simple_clothes_colab_training.ipynb), though you may have to tweak some paths to use it.

## Running

To run this locally, first copy the trained model weights file to the `models` directory and then do

```
export FLASK_APP=index.py
flask run
```
If you just want to see how the model works without running flask, you can look at this [demo notebook](https://github.com/adamaji/maskrcnn-benchmark/blob/simple_clothes/demo/simple_clothes_demo.ipynb).

The results of the trained model are largely constrained by the given dataset. The images used for training were all street images (where the clothes are being worn instead of laid flat) with most of the people being caucasian women. This translates to more difficulty generalizing to images with off-model clothes or images with other genders/skin tones, and better performance on the kinds of images like those in the training data. To mitigate this, a larger and more varied dataset of detections would be helpful.

