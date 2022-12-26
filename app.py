import streamlit as st
from PIL import *
import numpy as np
import cv2
import base64
# from tensorflow.keras import *
from night_images import illuminate


st.markdown('<h1 style="color:white;">Image Enhancement Model</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color:white;">This uses opencv to enhance the image given by extracting important features</h2>', unsafe_allow_html=True)


# background image to streamlit

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('P:\\Police Hackathon\\Glowpic\\content\\bg2.webp')

upload= st.file_uploader('Insert image for classification', type=['png','jpg'])
c1, c2= st.columns(2)
if upload is not None:
  im= Image.open(upload)
#   imgtf = load_image(im)
  
  img1= np.asarray(im)
  img= cv2.resize(img1,(224, 224))
  
  img= np.expand_dims(img, 0)
  
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)
  
  
  c2.header('Enhanced Image :')
  c2.image(illuminate().starter(img1))
# c2.write(classes[vgg_pred_classes[0]] )