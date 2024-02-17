from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from daily_summary.main import extract_git_data


class TestExtractGitData:
    @patch('daily_summary.main.git.Repo')
    def test_extract_git_data_with_start_and_end_dates(self, mock_repo):
        author = Mock()
        author.name = 'Test Author'
        mock_repo.return_value.iter_commits.return_value = [
            Mock(authored_datetime=datetime(2023, 4, 1), hexsha='abc123', author=author, message='Commit message 1'),
            Mock(authored_datetime=datetime(2023, 4, 2), hexsha='def456', author=author, message='Commit message 2'),
            Mock(authored_datetime=datetime(2023, 4, 3), hexsha='ghi789', author=author, message='Commit message 3'),
        ]
        diffs = extract_git_data('.', 'Test Author', '2023-04-02', start_date='2023-04-01', end_date='2023-04-03')
        assert len(diffs) == 3

    @patch('daily_summary.main.git.Repo')
    def test_extract_git_data_with_only_start_date(self, mock_repo):
        author = Mock()
        author.name = 'Test Author'
        mock_repo.return_value.iter_commits.return_value = [
            Mock(authored_datetime=datetime(2023, 4, 1), hexsha='abc123', author=author, message='Commit message 1'),
            Mock(authored_datetime=datetime(2023, 4, 2), hexsha='def456', author=author, message='Commit message 2'),
        ]
        diffs = extract_git_data('.', 'Test Author', '2023-04-02', start_date='2023-04-01', end_date=None)
        assert len(diffs) == 2

    @patch('daily_summary.main.git.Repo')
    def test_extract_git_data_with_only_end_date(self, mock_repo):
        author = Mock()
        author.name = 'Test Author'
        mock_repo.return_value.iter_commits.return_value = [
            Mock(authored_datetime=datetime(2023, 4, 2), hexsha='def456', author=author, message='Commit message 2'),
            Mock(authored_datetime=datetime(2023, 4, 3), hexsha='ghi789', author=author, message='Commit message 3'),
        ]
        diffs = extract_git_data('.', 'Test Author', '2023-04-02', start_date=None, end_date='2023-04-03')
        assert len(diffs) == 2

    @patch('daily_summary.main.git.Repo')
    def test_extract_git_data_with_no_dates(self, mock_repo):
        author = Mock()
        author.name = 'Test Author'
        mock_repo.return_value.iter_commits.return_value = [
            Mock(authored_datetime=datetime(2023, 4, 2), hexsha='def456', author=author, message='Commit message 2'),
        ]
        diffs = extract_git_data('.', 'Test Author', '2023-04-02')
        assert len(diffs) == 1

    @patch('daily_summary.main.git.Repo')
    def test_extract_git_data_with_invalid_date_range(self, mock_repo):
        mock_repo.return_value.iter_commits.return_value = []
        with pytest.raises(ValueError):
            extract_git_data('.', 'Test Author', '2023-04-02', start_date='2023-04-03', end_date='2023-04-01')
