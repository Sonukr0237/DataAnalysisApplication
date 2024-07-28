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
        
    st.subheader(':rainbow[Column Values To Count]', divider='rainbow')
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose Column name', options=list(data.columns))
        with col2:
            toprows = st.number_input('Top Rows', min_value=1, step=1)
           
        count = st.button('Count')
        if(count==True):
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualization', divider='gray')
            fig = px.bar(data_frame=result, x=column, y='count', text='count', template='plotly_white')
            st.plotly_chart(fig)
            fig = px.line(data_frame=result, x=column, y='count', text='count', template='plotly_white')
            st.plotly_chart(fig)
            fig = px.pie(data_frame=result, names = column, values = 'count')
            st.plotly_chart(fig)
    