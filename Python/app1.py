import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: #5CDB95;  # Replace with your preferred color
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header('AttenD `- A data analysis tool`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('Male', 'Female')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

# st.sidebar.subheader('Line chart parameters')
# plot_data = st.sidebar.multiselect('Select genders',options=["Male", "Female"],default=["Male", "Female"])
# plot_height = st.sidebar.slider('Specify plot height', 20, 50, 25)

#for response rate
# response_rate1 = np.divide(user_data['Voted_For_Stalls'], user_data['Registered_Accounts']) * 100
# response_ratef2 = np.divide(user_data['Voted_For_Stalls'], stall_data['Registered_Accounts']) * 100
# response_rate3 = np.divide(stall_data['Voted_For_Stalls'], stall_data['Registered_Accounts']) * 100
# response_rate = (response_rate1 + response_rate2 + response_rate3)/3

# response_rate = response_rate.round(2)




stall_data = pd.read_csv('./Data/stall_data.csv')
user_data = pd.read_csv('./Data/user_data.csv')

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

# with c1:
#     # Add your heatmap here
#     st.markdown('### Heatmap')
#     Heat = px.imshow(stall_data[['StallNumber', 'Likes', 'Dislikes']], 
#                     width=600, 
#                     height=400,
#                     color_continuous_scale='BUGN')
#     st.plotly_chart(Heat, use_container_width=True)

#ROW B

with c1:

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

with c2:
    # Add your pie chart here
    st.markdown('### Pie chart')
    likes_sum = stall_data.groupby('Department')['Likes'].sum().reset_index()
    colors = ['#05c793', '#ffb60a', '#1d3557']
    pie = px.pie(likes_sum, values='Likes', names='Department', color_discrete_sequence=colors, width=400, height=400)
    pie.update_layout(template="plotly")
    st.plotly_chart(pie, use_container_width=True)


# Row C
st.markdown('### Line chart')
user_data['RegTime'] = pd.to_datetime(user_data['RegTime'])
UserData = user_data.sort_values('RegTime')

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select genders', options=["Male", "Female"], default=["Male", "Female"])
plot_height = st.sidebar.slider('Specify plot height', 30, 100, 50)

time_range = st.sidebar.slider(
    'Select a range of registration times',
    9, 18, (9, 18)
)

mask = UserData.Gender.isin(plot_data)
user_data_filtered = UserData[mask].iloc[time_range[0]:time_range[1]]

total_registrations = UserData.groupby('RegTime')['CountoftheUser'].sum().reset_index()
total_registrations['Gender'] = 'Total'

final_data = pd.concat([user_data_filtered, total_registrations])

colors = {'Male': 'blue', 'Female': 'pink', 'Total': 'green'}

fig = px.line(final_data, x='RegTime', y='CountoftheUser', color='Gender', title='Event Registration Over Time', height=plot_height*10, color_discrete_map=colors)

st.plotly_chart(fig, use_container_width=True)

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