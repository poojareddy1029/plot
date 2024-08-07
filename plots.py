import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

chart_data= pd.DataFrame(np.random.randn(20,3), columns = ['Line-1', 'Line-2', 'Line-3'])
st.header('Chart_Data Table')
st.table(chart_data)

st.header('1. Charts with Random numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

st.header('2. Visualisation with Matplotlib and Seaborn')

st.subheader('2.1 Loading the DataFrame')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Graph with Matplotlib')
fig = plt.figure(figsize=(8,5))
df['variety'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution Plot with Seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal.length'])
st.pyplot(fig)

st.header('3. Multiple Graphs')
col1, col2 = st.columns(2)

with col1:
    col1.header = 'KDE=False'
    fig1 = plt.figure(figsize=(15,10))
    sns.distplot(df['sepal.length'], kde = False)
    st.pyplot(fig1)

with col2:
    col2.header = 'Hist= False'
    fig2 = plt.figure(figsize=(15,10))
    sns.distplot(df['sepal.length'], hist  = False)
    st.pyplot(fig2)

st.header('4. changing Style')
col1, col2 = st.columns(2)

with col1:
    fig = plt.figure(figsize=(15,10))
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal.length'], hist = False)
    st.pyplot(fig)

with col2:
    fig = plt.figure(figsize=(15,10))
    sns.set_theme(context= 'poster', style='darkgrid')
    sns.distplot(df['petal.length'], hist  = True)
    st.pyplot(fig)

st.header('5, Exploring Different Graphs of Seaborn')
st.subheader('5.1 Scatter Plot')
fig= plt.figure(figsize=(15,8))
plt.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize=(15,8))
sns.countplot(data= df, x='variety')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize=(15,8))
sns.boxplot(data= df, x= 'variety', y= 'petal.length')
st.pyplot(fig)

st.subheader('5.4 Voilin-PLot')
fig = plt.figure(figsize=(15,8))
sns.violinplot(data=df, x='variety', y='petal.length')
st.pyplot(fig)
