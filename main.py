import os
import numpy as np
import cv2
import pandas as pd
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


#def read_data():
    #return pd.read_csv(r"insurance.csv ")

#df=read_data()
#st.write(df)
if w1:
    st.write('Table')

    
df = pd.DataFrame(
np.random.randn(2, 5),
columns=('col %d' % i for i in range(5)))

st.dataframe(df)  # Same as st.write(df)
