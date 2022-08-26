import os
import numpy as np
import cv2
import pandas as pd
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title('Charge&Guess')
st.markdown('''
Please use input data
''')

#have to load model in ('')
#model = load_model('')

st.sidebar.title("Operations on the Dataset")

#st.subheader("Checkbox")
w1 = st.sidebar.checkbox("Sample data ", False)


#def read_data():
    #return pd.read_csv(r"insurance.csv ")

#df=read_data()
#st.write(df)
if w1:
    st.write('Sample data')
    image = Image.open('data_charges.png')
    st.image(image, 'Sample data')
'''
col1, col2, col3 , col4, col5, col6= st.columns(6)
    
with col1:
    st.header("Age")
    age = st.number_input('Insert age')
    st.write('The current number is ', age)
    
with col2:
    st.header("Sex")
    sex = st.selectbox(
     'gender',
     ('male', 'female'))

    st.write('You selected:', sex)
    
with col3:
    st.header("BMI")
    bmi = st.number_input('Insert bmi')
    st.write('The current number is ', bmi)
    
with col4:
    st.header("Child")
    children = st.number_input('Insert no of children')
    st.write('The current number is ', children)
    
with col5:
    st.header("smoker")
    smoker = st.selectbox(
     'smoker',
     ('yes', 'no'))

    st.write('You selected:', smoker)
    
    
with col6:
    st.header("region")
    region = st.selectbox(
     'Region',
     ('southeast', 'southwest','northeast','northwest'))

    st.write('You selected:', region)
    
'''

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Age")
    age = st.number_input('Insert age')
    st.write('The current number is ', age)
    
with col2:
    st.header("Sex")
    sex = st.selectbox(
     'gender',
     ('male', 'female'))

    st.write('You selected:', sex)
    
with col3:
    st.header("BMI")
    bmi = st.number_input('Insert bmi')
    st.write('The current number is ', bmi)


