import unittest
from unittest.mock import patch
from importlib.machinery import SourceFileLoader

class TestNumberOfSubscribers(unittest.TestCase):
    def setUp(self):
        module = SourceFileLoader("number_of_subscribers", "../0-subs.py").load_module()
        self.number_of_subscribers = module.number_of_subscribers

    @patch("number_of_subscribers.requests.get")
    def test_valid_subreddit(self, mock_get):
        # Mock the response for a valid subreddit
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "subscribers": 5000
            }
        }
        mock_get.return_value = mock_response

        # Call the function and assert the result
        result = self.number_of_subscribers("programming")
        self.assertEqual(result, 5000)

    @patch("number_of_subscribers.requests.get")
    def test_invalid_subreddit(self, mock_get):
        # Mock the response for an invalid subreddit
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the function and assert the result
        result = self.number_of_subscribers("invalidsubreddit")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
