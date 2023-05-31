### In terminal
# pip3 install streamlit
# pip3 install requests
# pip3 install pycountry

## FOR SUMMARISER
# xcode-select --install
# pip install --upgrade pip setuptools
# pip install cytoolz
# pip install cymem
# pip install murmurhash
# pip install preshed
# pip install thinc
# pip install spacy
# !pip install spacy==2.0.12
# !pip install transformers==2.2.0
# !pip install bert-extractive-summarizer
# pip3 install torch torchvision
# pip install --upgrade transformers


# To run app, type in terminal: streamlit run whatsnew_source.py

# ================================================================================================

# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pycountry
from PIL import Image
# from config import NEWS_API_KEY
from streamlit import secrets
from summarizer import Summarizer,TransformerSummarizer
from functions import get_all_news
from datetime import datetime, date, timedelta

# =============st===================================================================================

## DISPLAYING TEXT ---------------------------------------------------
# title / header / subheader / text / caption / code / text / markdown

# Giving the app a title

title = st.markdown("# THE BUZZ")
header = st.subheader("A home-grown news app")
st.markdown('*Here you can check for all news. If you specifically want __Top Headlines__, go to the next page from the sidebar!*')
# st.text('raw text')
# st.caption('caption')
# st.code('hfjkdckjdckjs')
# st.markdown('<h3>This is a normal writing<h3>', unsafe_allow_html=True)
# st.write('Normal writing')

# ================================================================================================

## Language ----------------------------------------------------

language_mapping = {
    'german': 'de',
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'italian': 'it',
    'portugese': 'pt',
    'dutch': 'nl'
}

# ================================================================================================

## DEFINING THE DIFFERENT GET-NEWS FUNCTIONS ACC. TO CONDITIONS ---------------------------------------------------

# defining the function to get all news

## FUNCTION IMPORTED
from functions import get_all_news

# ================================================================================================

## INPUTS ---------------------------------------------------

# User inputs -----------------------------------------------------------------------------
keyword = st.text_input('Keyword')
user_choice_language = st.selectbox('Select Language', ['German', 'English', 'Spanish','French', 'Italian', 'Portugese', 'Dutch'])
language = language_mapping.get(user_choice_language.lower())
sort_by = st.selectbox('Articles sorted by/according to:', ['', 'relevancy', 'popularity', 'publishedAt'])

# maximum allowed date (one month ago from today - News API limitations :))
today = date.today()
min_date = today - timedelta(days=30) # from
max_date = today - timedelta(days=1) # to

col1, col2 = st.columns(2) # to have two input boxes in one row

with col1:
    from_date = st.date_input('From which date', min_value=min_date, max_value=max_date, value=min_date)

with col2:
    to_date = st.date_input('To which date', min_value=min_date, max_value=max_date, value=max_date)

range_articles = st.slider('How many articles do you want?', 0, 10)
agree = st.checkbox('I agree with the terms and conditions')

## ==================================================================================

# The enter button to get news - what the if statement will trigger :)

button1 = st.button('Enter')
if button1:
    if keyword and language:
        articles = get_all_news(keyword, language, from_date, to_date, range_articles, sort_by)
        for article in articles:
            st.header(article['title'])
            st.write("Published at:", article['publishedAt'])
            st.write(article['source']['name'])
            if 'urlToImage' in article and article['urlToImage']:
                try:
                    image = Image.open(requests.get(article['urlToImage'], stream=True).raw)
                    st.image(article['urlToImage'])
                except:
                    st.write("Unable to display image.")
            else:
                st.write("No image available.")
            st.write(article['content'])
            st.markdown(f"[Read full article]({article['url']})")