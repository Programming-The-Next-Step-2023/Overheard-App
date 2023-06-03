### TESTING THE `get_all_news` function ====================================================================

# Libraries
import unittest
from functions import get_all_news
from unittest import mock
# using mocking/patching so we don't have to rely on the API (because results from API are prone to change)

# Testing

class TestGetAllNews(unittest.TestCase):
    @mock.patch('functions.requests.get') # mocks responses.get function (so we can test without the actual API)
    def test_get_all_news(self, mock_get):

        # Test inputs for the get_all_news function:
        keyword = "elections"
        language = "en"
        from_date = "2023-06-01"
        to_date = "2023-06-01"
        range_articles = 3
        sort_by = "publishedAt"

        # Creating mock answers (simulation of actual API response); this is the response we expect
        mock_response = {
            "articles": [
                {"title": "Kosovo: Nato ready to send more troops after unrest", "content": "Nato says it is ready to send more troops to Kosovo after unrest following the appointment of ethnic Albanian mayors to majority-Serb areas. Pristina and Belgrade have blamed each other for the unre… [+2265 chars]"},
                {"title": "Zimbabwe outlaws criticism of government before August elections", "content": "Zimbabwes parliament has outlawed criticism of the government before presidential and parliamentary elections in August, with violations of a new law punishable by up to 20 years in jail. The crimin… [+1203 chars]"},
                {"title": "The Guardian view on the snap Spanish election: Europe needs Sánchez’s gamble to pay off | Editorial", "content": "Spains socialist prime minister, Pedro Sánchez, has a reputation for judicious risk-taking. In 2018, after orchestrating a vote of no confidence in the incumbent centre-right government, he was appoi… [+3267 chars]"}
            ]
        }

        # Setting how we want mock response (--> JSON format as in the actual script)
        mock_get.return_value.json.return_value = mock_response

        # Calling function to test
        articles = get_all_news(keyword, language, from_date, to_date, range_articles, sort_by)

        # Assertions to check whether responses to the function (line 37) matches our mock responses
        self.assertEqual(articles, mock_response["articles"])

# Running the test
if __name__ == '__main__':
    unittest.main()



