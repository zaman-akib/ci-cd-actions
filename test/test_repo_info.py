import unittest
from unittest.mock import patch, Mock
from script.repo_info import *

class TestRepoInfo(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_latest_commit_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            'sha': 'abc123',
            'commit': {
                'message': 'Initial commit',
                'author': {
                    'name': 'John Doe',
                    'date': '2023-01-01T00:00:00Z'
                }
            }
        }]
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            fetch_latest_commit('owner', 'repo')
            mock_print.assert_any_call('Latest Commit sha: abc123\nMessage: Initial commit\nAuthor: John Doe, Date: 2023-01-01T00:00:00Z\n')

    @patch('requests.get')
    def test_fetch_latest_commit_network_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        with self.assertRaises(SystemExit):
            fetch_latest_commit('owner', 'repo')

    @patch('requests.get')
    def test_fetch_issues_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'title': 'Issue 1', 'state': 'open'}]
        mock_get.return_value = mock_response
        mock_response.links = {}

        with patch('builtins.print') as mock_print:
            fetch_issues('owner', 'repo', 20)
            mock_print.assert_any_call('Issue: Issue 1, Status: open')

    @patch('requests.get')
    def test_fetch_issues_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_response.links = {}
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            fetch_issues('owner', 'repo', 20)
            mock_print.assert_any_call('No open issues found')

    @patch('requests.get')
    def test_fetch_pull_requests_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'title': 'PR 1', 'state': 'open'}]
        mock_get.return_value = mock_response
        mock_response.links = {}

        with patch('builtins.print') as mock_print:
            fetch_pull_requests('owner', 'repo', 20)
            mock_print.assert_any_call('Pull Request: PR 1, Status: open')

    @patch('requests.get')
    def test_fetch_pull_requests_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response
        mock_response.links = {}

        with patch('builtins.print') as mock_print:
            fetch_pull_requests('owner', 'repo', 20)
            mock_print.assert_any_call('No open pull requests found')

if __name__ == '__main__':
    unittest.main()