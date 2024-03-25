import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
import matplotlib.pyplot as plt

import streamlit as st
import seaborn as sns
import pandas as pd

# Load data
onlinefoods_data = pd.read_csv('./data/onlinefoods.csv')

# Example table
st.subheader('ตัวอย่างตารางข้อมูล')
st.write(onlinefoods_data.head(10))

# Count by gender
st.subheader('จำนวนเพศตามช่วงอายุ')
sns.countplot(x='Gender', data=onlinefoods_data)  
plt.xlabel('เพศ')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()

# Sales by gender
st.subheader('ยอดขายตามเพศ')
sns.barplot(x='Gender', y='Sales', data=onlinefoods_data, estimator=sum)  
plt.xlabel('เพศ')
plt.ylabel('ยอดขายรวม')
plt.xticks(rotation=45)
st.pyplot()
