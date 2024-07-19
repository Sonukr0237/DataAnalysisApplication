import pandas as pd
import  plotly.express as px
import streamlit as st

st.set_page_config(
    page_title='My application for Data Anaysis',
    page_icon= '❗'
)

st.title(':rainbow[Data Analytics Portal]')
st.subheader(':grey[Explore Data with ease.]', divider='rainbow')

file = st.file_uploader('Drop CSV or Excel FIle', type=['csv', 'xlsx'])
if(file!=None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
        
    st.dataframe(data)
    st.info('File is successfully Uploaded',icon='🔥')