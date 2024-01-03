import streamlit as st
import pandas as pd
import numpy as np

logo = '<img style="width: 100px; position: absolute; top: 10px; right: 10px;" src="https://i.postimg.cc/FKqWr8BN/logo-attend.png">'
st.markdown(logo, unsafe_allow_html= True)

title = '<h1 style="font-family: Roboto; color:white; font-size: 55px; text-align: center">AttenD - A data analysis Tool </h1>'
st.markdown(title, unsafe_allow_html=True)

# Set the background image
img = """
<style>
[data-testid="stAppViewContainer"] > .main {
   background: hsla(0, 0%, 85%, 1);

background: linear-gradient(0deg, hsla(0, 0%, 85%, 1) 0%, hsla(191, 88%, 13%, 1) 0%, hsla(77, 33%, 92%, 1));

background: -moz-linear-gradient(0deg, hsla(0, 0%, 85%, 1) 0%, hsla(191, 88%, 13%, 1) 0%, hsla(77, 33%, 92%, 1));

background: -webkit-linear-gradient(0deg, hsla(0, 0%, 85%, 1) 0%, hsla(191, 88%, 13%, 1) 0%, hsla(77, 33%, 92%, 1));

</style>
"""
st.markdown(img, unsafe_allow_html=True)
