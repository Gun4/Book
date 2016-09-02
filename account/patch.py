from account import *
import unittest
from mock import Mock, patch


class TestAccount(unittest.TestCase):

    @patch('Pytest_book.account.requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Some text data'
        mock_requests.get.return_value = mock_response
        account = Account(Mock())
        self.assertEqual({'status': 200, 'data': 'Some text data'}, account.get_current_balance('1'))
