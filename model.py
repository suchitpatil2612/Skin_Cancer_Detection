"""This module load the model and return it"""
import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model("SkinCancer.h5")
  return model