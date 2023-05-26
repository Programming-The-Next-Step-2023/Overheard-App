### In terminal
# pip3 install streamlit
# pip3 install requests
# pip3 install pycountry

# To run app, type in terminal: streamlit run whatsnew_source.py

# ================================================================================================

# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pycountry
from PIL import Image
from config import NEWS_API_KEY

# =============st===================================================================================

## DISPLAYING TEXT ---------------------------------------------------
# title / header / subheader / text / caption / code / text / markdown

# Giving the app a title
title = st.title("What's buzzing today?")
# st.header('Header')
# st.subheader('subheader')
# st.text('raw text')
# st.caption('caption')
# st.code('hfjkdckjdckjs')
# st.markdown('<h3>This is a normal writing<h3>', unsafe_allow_html=True)
# st.write('Normal writing')


# ================================================================================================

## INPUTS ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    country_name = st.text_input('Country name')

with col2:
    keyword = st.text_input('Keyword')

from_date = st.date_input('From which date') # date input on Streamlit only appears to go back to 2013
to_date = st.date_input('To which date (enter a date only upto a month back!)')
# maybe add a custom date picker / data range?

# ================================================================================================

## DISPLAYING INTERACTIVE WIDGETS ---------------------------------------------------
# button / download button / ....


# st.radio('Category', ('business', 'politics', 'sports'))
# st.selectbox('Choose category', ['business', 'politics', 'sports'])

## for multiple options
st.multiselect('Choose category', ['Business', 'Politics', 'Sports', 'Technology', 'Celebrities / Gossip'])

# slider / select_slider
range = st.slider('How many articles do you want?', 0, 20)

agree = st.checkbox('I agree with the terms and conditions')

button1 = st.button('Enter')
if button1:
    # country = pycountry.countries.get(name=country_name).alpha_2
    url = 'https://newsapi.org/v2/everything?'
    parameters = { 
    'q': keyword, # query phrase
    'from': from_date,
    'to': to_date,
    'pageSize': range,  # maximum is 100
    'apiKey': NEWS_API_KEY # your own API key
    }
    # what format does it return it in? if it's hard to get pics, then remove it
    response = requests.get(url, params=parameters)
    response_json = response.json()
    articles = response_json['articles']
    for article in articles:
        st.header(article['title'])
        st.write("Published at:", article['publishedAt'])
        #if article['author']:
            # st.write(article['author'])
        st.write(article['source']['name'])
        # st.write(article['description'])
        # st.image(article['urlToImage'])
        if 'urlToImage' in article and article['urlToImage']:
            try:
                image = Image.open(requests.get(article['urlToImage'], stream=True).raw)
                st.image(article['urlToImage'])
            except:
                st.write("Unable to display image.") # italics?? colour?

        st.write(article['content'])
        st.markdown(f"[Read full article]({article['url']})")


# ================================================================================================

## LAYOUTS ---------------------------------------------------

# expander
# with st.expander('Click here'):
   # st.metric('Temp', "20", -9)

# sidebar (!! nice)
# st.sidebar.title("What's Buzzing?")




