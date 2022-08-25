import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title('Charge&Guess')
st.markdown('''
Please use input data
''')

#have to load model in ('')
#model = load_model('')

st.sidebar.title("Operations on the Dataset")

#st.subheader("Checkbox")
w1 = st.sidebar.checkbox("show table", False)
plot= st.sidebar.checkbox("show plots", False)
plothist= st.sidebar.checkbox("show hist plots", False)
trainmodel= st.sidebar.checkbox("Train model", False)
dokfold= st.sidebar.checkbox("DO KFold", False)
distView=st.sidebar.checkbox("Dist View", False)
_3dplot=st.sidebar.checkbox("3D plots", False)
linechart=st.sidebar.checkbox("Linechart",False)
#st.write(w1)

def read_data():
    return pd.read_csv("")

df=read_data()

if w1:
    st.dataframe(df,width=2000,height=500)
