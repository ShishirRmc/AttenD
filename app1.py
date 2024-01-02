import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


    
st.sidebar.header('AttenD `- A data analysis tool`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('Male', 'Female')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['male', 'female'], ['male', 'female'])
plot_height = st.sidebar.slider('Specify plot height', 20, 50, 25)

#for response rate
# response_rate1 = np.divide(user_data['Voted_For_Stalls'], user_data['Registered_Accounts']) * 100
# response_ratef2 = np.divide(user_data['Voted_For_Stalls'], stall_data['Registered_Accounts']) * 100
# response_rate3 = np.divide(stall_data['Voted_For_Stalls'], stall_data['Registered_Accounts']) * 100
# response_rate = (response_rate1 + response_rate2 + response_rate3)/3

# response_rate = response_rate.round(2)




stall_data = pd.read_csv('stall_data.csv')
user_data = pd.read_csv('user_data.csv')

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)

total_registered = len(user_data)
user_data['RegTime'] = pd.to_datetime(user_data['RegTime'])
now = datetime.now()
ten_seconds_apx = now - timedelta(seconds=10)
recent_users = user_data[user_data['RegTime'] > ten_seconds_apx]
recent_users = len(recent_users)
col1.metric("Total Registered", total_registered, recent_users)

col2.metric("Average Age", "average", "-8%")
col3.metric("Response Rate", "86%", "4%")
c1, c2 = st.columns((7,3))

with c1:
    # Add your heatmap here
    st.markdown('### Heatmap')
    Heat = px.imshow(stall_data[['StallNumber', 'Likes', 'Dislikes']], 
                    width=600, 
                    height=400,
                    color_continuous_scale='BUGN')
    st.plotly_chart(Heat, use_container_width=True)

with c2:
    # Add your pie chart here
    st.markdown('### Pie chart')
    likes_sum = stall_data.groupby('Department')['Likes'].sum().reset_index()
    colors = ['Red', 'Green', 'Blue']
    pie = px.pie(likes_sum, values='Likes', names='Department', title='Pie', color_discrete_sequence=colors, width=400, height=400)
    st.plotly_chart(pie, use_container_width=True)


# Row C
st.markdown('### Line chart')
gender_count = user_data['Gender'].value_counts().reset_index()

# Rename the columns
gender_count.columns = ['Gender', 'Count']

# Create the line chart
line_chart = px.line(gender_count, x='Gender', y='Count', title='Number of Males and Females')
st.plotly_chart(line_chart, use_container_width=True)

#Row D
st.markdown('### BarChart Diagram')
Bar = st.columns(1)
likes_bar = go.Bar(
    x=stall_data['StallName'],
    y=stall_data['Likes'],
    name='Likes',
    marker_color='blue'
)

Dislikes_bar = go.Bar(
    x=stall_data['StallName'],
    y=stall_data['Dislikes'],
    name='Dislikes',
    marker_color='red'
)
data = [likes_bar, Dislikes_bar]
layout = go.Layout(
    title='Likes and Dislikes for Each Stall',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig)