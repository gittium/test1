import streamlit as st
import pandas as pd
import plotly.express as px

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('Advertising.csv')

st.header("🤖💸 Ads Price Predictor 💸🤖")
# ตั้งค่า Sidebar
title = st.sidebar.subheader('ใส่จำนวน units TV ที่ต้องการทำนาย ', divider='rainbow')
x_pre = st.sidebar.text_input('Units: ','')
button = st.sidebar.button("Predict","primary")
if button:
    y = 7.443040536235991 + 0.04466639703815767 * float(x_pre)
    st.write(f"ราคาที่คาดว่าจะได้จากการทำโฆษณาคือ: {round(y, 4)}")
else:
    st.warning("👈👈กรุณาใส่จำนวน units ที่ต้องการทางซ้ายมือ")



title1 = st.sidebar.subheader('เลือกดูกราฟของข้อมูลตามต้องการ', divider='rainbow')
x_column = st.sidebar.selectbox('เลือก X', df.columns)
y_column = st.sidebar.selectbox('เลือก Y', df.columns)

# สร้าง Scatter Plot ด้วย Plotly
fig = px.scatter(df, x=x_column, y=y_column, title=f"Scatter Plot ระหว่าง {x_column} และ {y_column}")
st.plotly_chart(fig)

