import streamlit as st
import pandas as pd

import numpy as np
st.title('🤫🧏 Iris flower')
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')
# st.write(df)
st.sidebar.subheader('Enter your age')
value = st.sidebar.text_input('')

if value:
    st.subheader(f"You're {value} yo")
    st.warning(value)
    rdata = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')
    st.write(rdata)
    rdata2 = rdata.groupby('Species').mean()
    st.write(rdata2)
    
    st.scatter_chart(rdata2)
    


else:
    st.subheader('👈 Please enter your age')
    st.error('i will guess your age!')
    
