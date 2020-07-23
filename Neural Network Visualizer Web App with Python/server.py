import json
import numpy as np
import os
import tensorflow as tf
import random
import string
from flask import Flask, request

app = Flask(__name__)

model = tf.keras.models.load_model('NNmodel.h5')
feature_model = tf.keras.models.Model(model.inputs, [layer.output for layer in model.layers[1:]])

_, (x_test, _) = tf.keras.datasets.mnist.load_data()
_, w, h = x_test.shape
x_test = x_test / 255.

def get_prediction():
    index = np.random.choice(x_test.shape[0])
    image = x_test[index, :, :]
    image_arr = np.reshape(image, (1, w*h))
    return feature_model.predict(image_arr), image

@app.route('/server', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        preds, image = get_prediction()
        final_preds = [p.tolist() for p in preds]
        return json.dumps({'prediction':final_preds, 'image':image.tolist()})
    return "Welcome..!"

if __name__ == '__main__':
    app.run()