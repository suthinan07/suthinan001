import streamlit as st
import pandas as pd
# Load data
onlinefoods_data = pd.read_csv('./data/onlinefoods.csv')

# Example table
st.subheader('ตัวอย่างตารางข้อมูล')
st.write(onlinefoods_data.head(10))

# Count by gender
st.subheader('จำนวนเพศตามช่วงอายุ')
st.bar_chart(onlinefoods_data['Gender'])
sns.countplot(x='Gender', data=onlinefoods_data)  
plt.xlabel('เพศ')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()

# Sales by gender
st.subheader('ยอดขายตามเพศ')
st.bar_chart(onlinefoods_data.groupby('Gender')['Sales'].sum())
plt.xlabel('เพศ')
plt.ylabel('ยอดขายรวม')
plt.xticks(rotation=45)
st.pyplot()
