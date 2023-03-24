import streamlit as st  # per lanciare frontend
import pandas as pd
import numpy as np

from PIL import Image

st.text("Ciao questo front-end funziona")

st.dataframe(pd.DataFrame({
    'first column': [1,2,3],
     'second column':[4,5,6] ,
    }))
st.dataframe(pd.DataFrame({
    'Name':['Jack','James','David'],
    'Surname':['Brown','Smith','Beckhem']

}))

image = Image.open('pacific-coast.jpg')

st.image(image, caption='Pacific coast',width=100)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

genre=st.radio(" Write your favourite dish",
               ('Pizza','Pasta','Insalata'))

if genre =='Pizza':
    st.write('Your order is confirmed')
else:
    st.write('Make your order ')    

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (10.0, 50.0))
st.write('Values:', values)

age=st.slider('How old are you?', 0, 30, 34)
st.write("I am ", age ,'years old')