"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
import numpy as np

import tensorflow as tf
from tensorflow.keras import preprocessing
from PIL import Image

from model import load_model

def app():
    """This funciton runs the prediction page"""

    # Create label values for the prediction
    label = ['actinic keratosis', 'basal cell carcinoma', 'dermatofibroma', 'melanoma', 'nevus', 
            'pigmented benign keratosis', 'seborrheic keratosis', 'squamous cell carcinoma', 'vascular lesion']

    # Take image input
    image = st.file_uploader("Upload Skin Cancer Image", type=['png','jpeg', 'jpg'])

    # If image then show the image and preprocess it.
    if image:
        st.image(image)
        img = Image.open(image)
        img = tf.image.resize(img, [256, 256])
        img = preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        # load the model
        model = load_model()

        # predict value
        pred_value = ""
        prediction = model.predict(img)

        if (np.max(prediction) < 0.95):
            pred_value = "Cancer not detected"
        else:
            pred_value = label[np.argmax(prediction)]

        # Show prediction values
        if not (pred_value == "Cancer not detected"):
            st.success("Prediction successful!!!")
            st.success(f"Predicted Skin Cancer is '{pred_value}'")
        else:
            st.error(f'{pred_value}!!!')
