import os
import sys
import unittest
from unittest.mock import patch

from daily_summary.main import check_env, main


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

if __name__ == '__main__':
    unittest.main()
