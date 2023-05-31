# Testing the function

import pytest
from functions import get_all_news

def test_get_news():
    # Test case 1: Valid inputs
    keyword = "technology"
    language = "en"
    from_date = "2022-01-01"
    to_date = "2022-01-10"
    range_dates = 5
    sort_by = "popularity"

    articles = get_all_news(keyword, language, from_date, to_date, range_dates, sort_by)
    
    assert isinstance(articles, list)
    assert len(articles) == range_dates  # Assuming the API returns the requested number of articles
    
