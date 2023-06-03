### In terminal
# pip3 install streamlit
# pip3 install requests
# pip3 install pycountry

## Note: To run app, type in terminal:
    # streamlit run the-buzz-dir/01_Welcome.py

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

# Title, header, instructions: -----------------------

# Giving the app a title, sub-header
title = st.markdown("# THE BUZZ")
header = st.subheader("A home-grown news app")

# Instructions
st.markdown('*Here you can check for all news. If you specifically want __Top Headlines__, go to the next page from the sidebar!*')

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

# Keyword: ------
keyword = st.text_input('Keyword*')
st.markdown("*You may also use more keywords by joining them using AND and OR.*")

user_choice_language = st.selectbox('Select Language*', ['German', 'English', 'Spanish','French', 'Italian', 'Portugese', 'Dutch'])
language = language_mapping.get(user_choice_language.lower())

# Sort by: ------
sort_by = st.selectbox('Articles sorted by/according to: (optional)', ['', 'relevancy', 'popularity', 'publishedAt'])

# Date: ------
# maximum allowed date (one month ago from today - News API limitations :))
today = date.today()
min_date = today - timedelta(days=30) # from
max_date = today - timedelta(days=1) # to

col1, col2 = st.columns(2) # to have two input boxes in one row

with col1:
    from_date = st.date_input('From which date', min_value=min_date, max_value=max_date, value=min_date)

with col2:
    to_date = st.date_input('To which date', min_value=min_date, max_value=max_date, value=max_date)

st.markdown("*Due to NewsAPI limitations, you can only search for news up to a month back.*")

# Article number: ----
range_articles = st.slider('How many articles do you want?', 0, 10)

# T&C:
agree = st.checkbox('I agree with the terms and conditions*')
st.write("Find T & C at the bottom of the page")

## ==================================================================================

# The enter button to get news - what the if statement will trigger :)

button1 = st.button('Enter')
if button1:

    # catching error (#1): users need to agree to terms and conditions
    if not agree:
        st.error("Please agree to the terms and conditions.")

    # catching error (#2): users need to enter keyword
    if agree:
        if not keyword:
            st.error("Please enter a keyword to proceed and get news!")

        else:
            articles = get_all_news(keyword, language, from_date, to_date, range_articles, sort_by)
            
            # if nothing shows up / there is an issue:
            if not articles:
                st.write("No articles found for the provided keyword.")
                st.write("1. Please check that the keyword is in the language you want the news article in.")
                st.write("2. If that does not work, then there probably have been too many news requests today, and you will have to try again tomorrow! Sorry!")
                
            # else print articles as usual:
            else:
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