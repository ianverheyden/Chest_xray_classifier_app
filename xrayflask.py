#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request, jsonify, url_for
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import random


# In[ ]:


app = Flask(__name__)

# Load the Chest X-Ray Predictor model
model = tf.keras.models.load_model('./models/binary_mobilnet_transferlearn_checkpoint.h5')
# Path to your test images
test_images_path = os.path.join(app.static_folder, 'test_images')

@app.route('/')
def index():
    # List of image names in the test dataset
    test_images = os.listdir(test_images_path)
    # Select a random subset of images to display
    displayed_images = random.sample(test_images, 3)
    return render_template('index2.html', displayed_images=displayed_images)

    
@app.route('/refresh-images', methods=['GET'])
def refresh_images():
    test_images = os.listdir(test_images_path)
    displayed_images = random.sample(test_images, 5)
    image_paths = [url_for('static', filename=f'test_images/{image}') for image in displayed_images]
    return jsonify(image_paths)


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files:
        file = request.files['file']
    else:
        # Handle case where user selects an image
        image_name = request.form['image_name']
        file_path = os.path.join(test_images_path, image_name)
        file = open(file_path, 'rb')

    if file:
        # Read and preprocess the image
        image = Image.open(io.BytesIO(file.read()))
        # Convert to RGB if the image is grayscale
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((224, 224))  # Resize as per model requirement
        image = np.array(image)
        image = np.expand_dims(image, axis=0)  # Model expects a batch

        # Make a prediction
        pred = model.predict(image)

        # Process prediction and generate a meaningful response
        prediction = 'Positive' if pred[0][0] > 0.5 else 'Negative'

        return prediction

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)

