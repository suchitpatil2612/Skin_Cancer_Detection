"""This is about page"""

# import necessary modules
import streamlit as st


def app():
    """This function runs the about page"""
    # Add balloons animation when page opens
    st.balloons()

    # Add title
    st.title("Welcome to the about me page")

    # Add an image
    st.image("./images/cancer_prediction.jpg")
    
    # Add Contact Details
    st.header('Contact Us')

    # Add email
    st.markdown('''### Name:
    Suchit Patil''')

    # Add name
    st.markdown('''### Email:
    suchitpatil2612@gmail.com''')

    # Add github
    st.markdown('''### GitHub: [SuchitPatil](https://github.com/suchitpatil2612)''')

    # Add linkedin
    st.markdown('''### Linkedin: [SuchitPatil](https://www.linkedin.com/in/suchit-p/)''')