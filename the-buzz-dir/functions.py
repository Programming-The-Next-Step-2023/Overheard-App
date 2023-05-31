# ============================ FUNCTIONS FOR MY NEWS APP ===============================

import streamlit as st
import pandas as pd
import numpy as np
import requests
import pycountry
from PIL import Image
# from config import NEWS_API_KEY
from streamlit import secrets
from datetime import datetime


### WELCOME PAGE ==========================================
# Page where users can acess ALL NEWS 

# This function is to get news using the 'everything' endpoint from the News API using keyword, language and sortBy
# function is called get_all_news

def get_all_news(keyword, language, from_date, to_date, range_articles, sort_by):
    url = 'https://newsapi.org/v2/everything?'
    parameters = { 
        'q': keyword, 
        'language': language,
        'from': from_date,
        'to': to_date,
        'pageSize': range_articles,  # 0 - 100
        'apiKey': st.secrets["NEWS_API_KEY"] # your own API key
    }
    
    if sort_by:
        parameters['sortBy'] = sort_by
    
    response = requests.get(url, params=parameters)
    response_json = response.json()
    articles = response_json.get('articles', [])
    
    return articles

# ====================================================================================
# ====================================================================================


### TOP HEADLINES PAGE ==========================================
# Page where users can acess TOP HEADLINES

# This function is to get news using the 'top-headlines' endpoint from the News API
# function is called get_top_headlines


def get_top_headlines(keyword_top, category, language_top, from_date_top, to_date_top, range_top):
    url_top = 'https://newsapi.org/v2/top-headlines?'
    parameters = { 
        'q': keyword_top, 
        'category': category,
        'language': language_top,
        'from': from_date_top,
        'to': to_date_top,
        'pageSize': range_top,  # 0 - 100
        'apiKey': st.secrets["NEWS_API_KEY"] # your own API key
    }
    
    response = requests.get(url_top, params=parameters)
    response_json = response.json()
    articles = response_json['articles']
    
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

