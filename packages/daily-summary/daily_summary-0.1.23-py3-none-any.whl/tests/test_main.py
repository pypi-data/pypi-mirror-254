import os
import sys
import unittest
from unittest import mock
from unittest.mock import patch

from daily_summary.main import check_env, extract_git_data, main


class TestMain(unittest.TestCase):

    @patch('os.environ.get')
    @patch('sys.stderr')
    @patch('sys.exit')
    def test_openai_api_key_not_set(self, mock_exit, mock_stderr, mock_environ_get):
        mock_environ_get.return_value = None
        check_env()
        mock_stderr.write.assert_called_once_with(
            "Error: OPENAI_API_KEY environment variable is not set. Please set the variable and try again.\n"
        )
        mock_exit.assert_called_once_with(1)

    def test_extract_git_data_ignores_different_dates(self):
        with mock.patch('git.Repo') as mock_repo:
            # Create mock commits with different dates and same authors
            mock_commit_different_date = mock.Mock()
            mock_commit_different_date.hexsha = 'abc1234'
            mock_commit_different_date.authored_datetime = mock.Mock()
            mock_commit_different_date.authored_datetime.date.return_value = mock.Mock()
            mock_commit_different_date.authored_datetime.date.return_value.strftime.return_value = '2022-01-01'
            mock_commit_different_date.author.name = 'John Doe'

            mock_commit_same_date = mock.Mock()
            mock_commit_same_date.hexsha = 'def5678'
            mock_commit_same_date.authored_datetime = mock.Mock()
            mock_commit_same_date.authored_datetime.date.return_value = mock.Mock()
            mock_commit_same_date.authored_datetime.date.return_value.strftime.return_value = '2023-01-01'
            mock_commit_same_date.author.name = 'John Doe'

            # Mock iter_commits method to return commits
            mock_repo.iter_commits.return_value = [mock_commit_different_date, mock_commit_same_date]

            # Call the extract_git_data with mock data
            diffs = extract_git_data('/fake/repo_path', 'John Doe', '2023-01-01')

            # Assert that diffs do not contain commit with a different date
            self.assertNotIn(mock_commit_different_date.hexsha, [diff['commit_hash'] for diff in diffs])

            # Assert that diffs only contain commits with the same date
            self.assertIn(mock_commit_same_date.hexsha, [diff['commit_hash'] for diff in diffs])
        self.assertEqual(1, 0)


if __name__ == '__main__':
    unittest.main()
