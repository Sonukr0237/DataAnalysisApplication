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
    st.info('File is Successfully Uploaded',icon='🔥')
    
    st.subheader(':rainbow[Basic information of dataset.]', divider='rainbow')
    
    tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])
    
    with tab1:
        st.write(f'There are {data.shape[0]} rows in dataset and {data.shape[1]} Columns in the dataset') 
        st.subheader(':grey[Statistical Summary of the dataset]')
        
    with tab2:
        st.subheader(':grey[Top Row]')
        top_rows = st.slider('Number of rows you want', 1, data.shape[0], key='topSlider')
        st.dataframe(data.head(top_rows))
        
        st.subheader(':grey[Bottom Row]')
        bottom_rows = st.slider('Number of rows you want', 1, data.shape[0], key='bottomSlider')
        st.dataframe(data.tail(bottom_rows))
        
    with tab3:
        st.subheader(':grey[Data types of columns]')
        st.dataframe(data.dtypes)
        
    with tab4:
        st.subheader(':grey[Column names in dataset]')
        st.write(list(data.columns))