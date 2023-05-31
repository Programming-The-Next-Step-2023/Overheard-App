
# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pycountry
from PIL import Image
# from config import NEWS_API_KEY
from streamlit import secrets
from functions import get_top_headlines
from datetime import datetime, date, timedelta

st.markdown("# Top Headlines")

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

## INPUTS ---------------------------------------------------

st.markdown("*You must enter a date range and language in which you want articles. In addition to these, you can optionally add keywords, countries and categories (you may add either 1, 2 or all 3 of these.)*")

# User inputs
keyword_top = st.text_input('Keyword (optional)')
# country_name = st.text_input('Country (optional)')
# country = pycountry.countries.get(name=country_name).alpha_2
category_options = [''] + ['business', 'entertainment', 'general', 'health', 'science', 'sport', 'technology']
category = st.selectbox('Choose Category (optional)', category_options)
user_choice_language_top = st.selectbox('Select Language*', ['German', 'English', 'Spanish','French', 'Italian', 'Portugese', 'Dutch'])  # User selects language from the dropdown

# Convert user input to the corresponding NewsAPI language value
language_top = language_mapping.get(user_choice_language_top.lower())

today = date.today()
min_date_top = today - timedelta(days=30)

st.text('Date range should be in the current month!')
col1, col2 = st.columns(2)

with col1:
    from_date_top = st.date_input('From which date', min_value=min_date_top, max_value=today, value=min_date_top)

with col2:
    to_date_top = st.date_input('To which date', min_value=min_date_top, max_value=today, value=today)


# ================================================================================================

## FUNCTION from functions.py
from functions import get_top_headlines

# slider / select_slider
range_top = st.slider('How many articles do you want?', 0, 10)

agree = st.checkbox('I agree with the terms and conditions')

button2 = st.button('Enter')
if button2:
    
    if button2:
        if keyword_top and language_top:
            get_top_headlines(keyword_top, None, language_top.lower(), from_date_top, to_date_top, range_top)
        elif keyword_top and category and language_top:
            get_top_headlines(keyword_top, category, language_top, from_date_top, to_date_top, range_top)
        elif category and language_top:
            get_top_headlines(None, category, language_top, from_date_top, to_date_top, range_top)
        elif language_top:
            get_top_headlines(None, None, language_top, from_date_top, to_date_top, range_top)
