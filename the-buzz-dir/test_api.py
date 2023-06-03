### TESTING THE API REQUESTS ====================================================================
# testing if I am able to use my API key to make requests

# Libraries
import unittest
import requests
from config import NEWS_API_KEY # stored the key here as well as in secrets.toml
from functions import get_all_news

# Testing
class TestAPI(unittest.TestCase):
    def test_api_requesting(self):

        # Make a request to the API
        ## NOTE: change date to one day earlier than when you're testing 
            # (e.g. you are testing on 2023-09-05, please change from= and to= to 2023-09-04)
        url = f'https://newsapi.org/v2/everything?q=health&from=2023-06-02&to=2023-06-02&apiKey={NEWS_API_KEY}'
        response = requests.get(url)

        # Checking if response is successful
        # HTTP status code '200 - OK' means that the "request was executed successfully"
        self.assertEqual(response.status_code, 200)
        # Thus, this indicates that there were no issues with requesting from the NewsAPI

if __name__ == '__main__':
    unittest.main()

## NOTE: the NewsAPI free plan can only allow for 100 API requests a day, so this must be taken into account while testing & using the app
