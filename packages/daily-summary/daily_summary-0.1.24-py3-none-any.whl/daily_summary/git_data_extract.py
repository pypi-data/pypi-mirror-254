import git
from datetime import datetime
import json


# Replace with your repository's path
def extract_git_data(repo_path, author, date):
    repo = git.Repo(repo_path)

    first_commit = list(repo.iter_commits())[-1].hexsha

    diffs = []
    for commit in repo.iter_commits():
        commit_date = commit.authored_datetime.date().strftime("%Y-%m-%d")
        if commit_date == date and commit.author.name == author:
            diff_data = {
                "commit_hash": commit.hexsha,
                "author": commit.author.name,
                "date": str(commit.authored_datetime),
                "message": commit.message.strip(),
                "diff": repo.git.diff(commit.hexsha + "^", commit.hexsha)
                if first_commit != commit.hexsha
                else "First Commit",
            }
            diffs.append(diff_data)

    # Writing diffs to a file
    with open("diffs.json", "w") as file:
        json.dump(diffs, file, indent=4)
