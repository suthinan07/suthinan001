import streamlit as st
import pandas as pd
# Load data
onlinefoods_data = pd.read_csv('./data/onlinefoods.csv')

# Example table
st.subheader('ตัวอย่างตารางข้อมูล')
st.write(onlinefoods_data.head(10))

# Count by gender
st.subheader('จำนวนเพศตามช่วงอายุ')
st.pyplot(sns_countplot)
plt.xlabel('เพศ')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()

# Sales by gender
st.subheader('ยอดขายตามเพศ')
sns_barplot = sns.barplot(x='Gender', y='Sales', data=onlinefoods_data, estimator=sum)
st.pyplot(sns_barplot)
plt.xlabel('เพศ')
plt.ylabel('ยอดขายรวม')
plt.xticks(rotation=45)
st.pyplot()
