import argparse
from datetime import datetime
import logging
import git
from tqdm import tqdm
import os
import sys
from openai import OpenAI

client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]

def extract_git_data(repo_path, author, date, start_date=None, end_date=None):
    repo = git.Repo(repo_path)

    commits = list(repo.iter_commits())
    if not commits:
        raise ValueError("No commits found in the repository.")
    first_commit = list(repo.iter_commits())[-1].hexsha

    author = author if author is not None else get_local_git_author(repo_path)
    if not author:
        logging.error(
            "Author name could not be inferred from local git configuration and was not provided as an argument."
        )
        exit(1)

    seen_commits = set()
    diffs = []
    if start_date is not None:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    if end_date is not None:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    # Convert start_date and end_date from string to date objects only once
    for commit in repo.iter_commits():
        if commit.hexsha in seen_commits:
            continue
        seen_commits.add(commit.hexsha)


        commit_date = commit.authored_datetime.date()
        diff_data = {
                "commit_hash": commit.hexsha,
                "author": commit.author.name,
                "date": str(commit.authored_datetime),
                "message": commit.message.strip(),
                
            }
        try:
            if first_commit != commit.hexsha:
                diff_data["diff"] = repo.git.diff(commit.hexsha + "^", commit.hexsha)
            else:
                diff_data["diff"] = repo.git.show(commit.hexsha) 
        except git.exc.GitCommandError:
            logging.error(f"Could not retrieve the diff for commit {commit.hexsha}.")
            continue
        if start_date and end_date and (start_date <= commit_date <= end_date) and commit.author.name == author:
            # If both start_date and end_date are provided, check if commit date is in the range
            diffs.append(diff_data)
        elif not start_date and end_date and commit_date <= end_date and commit.author.name == author:
            # If start_date is None, do up to end_date
            diffs.append(diff_data)
        elif not end_date and start_date and commit_date >= start_date and commit.author.name == author:
            # If end_date is None, do from start_date
            diffs.append(diff_data)
        elif not start_date and not end_date and commit_date == date and commit.author.name == author:
            # If both start_date and end_date are None, behave as before
            diffs.append(diff_data)
           

    return diffs


def get_local_git_author(repo_path):
    try:
        repo = git.Repo(repo_path, search_parent_directories=True)
        config_reader = repo.config_reader()
        author_name = config_reader.get_value("user", "name", None)
        return author_name
    except (
        git.exc.InvalidGitRepositoryError,
        git.exc.NoSuchPathError,
        git.exc.GitCommandError,
        KeyError,
    ):
        logging.error(
            "Could not retrieve the author name from the local git configuration."
        )
        return None



def summarize_diff(diff, model_name="gpt-4"):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": 'Summarize the key changes in this code diff. Don\'t say " the key changes are this" just say the key changes.',
            },
            {
                "role": "user",
                "content": diff,
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


def summarize_all_diffs(diffs, model_name):
    # Summarize the diffs
    summaries = ""
    for i, diff_data in tqdm(enumerate(diffs, start=1)):
        diff_summary = summarize_diff(diff_data["diff"], model_name)
        summaries += f"{i}. Commit: {diff_data['commit_hash']}\n"
        summaries += f"   Branch: {diff_data['branch']}\n"
        summaries += f"   Date: {diff_data['date']}\n"
        summaries += f"   Message: {diff_data['message']}\n"
        summaries += f"   Key Changes: {diff_summary}\n"
        summaries += "-" * 40 + "\n"
    return summaries


def daily_summary(summaries, author, date, model_name="gpt-4"):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": f"Create a daily development report for ${author}'s commits on {date}. The recipient of this report is Jack Driscoll. The report should start \"Your day in review\" followed by the top development updates of the day. Don't list by commit, but just give a holistic report of the day.  Here are the key changes made in each commit: ",
            },
            {
                "role": "user",
                "content": summaries,
            },
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


def generate(summaries, author, date, model_name):
    # Summarize the diffs
    report = daily_summary(summaries, author, date, model_name)
    print(report)
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate daily development reports.")
    check_env()
    parser.add_argument(
        "--repo",
        help="Path to the repository to generate the report for",
        default=".",
    )
    parser.add_argument(
        "--author",
        help="Name of the author to generate the report for",
        required=False,
    )
    parser.add_argument(
        "--date",
        help="Date for the report in YYYY-MM-DD format",
        default=datetime.now().date().strftime("%Y-%m-%d"),
    )
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="OpenAI model to be used for generating summaries",
    )
    parser.add_argument(
        "--start-date",
        help="Start date for the report range in YYYY-MM-DD format, defaults to None",
        default=None,
    )
    parser.add_argument(
        "--end-date",
        help="End date for the report range in YYYY-MM-DD format, defaults to None",
        default=None,
    )
    args = parser.parse_args()
    print("Generating daily development report...")
    print("Extracting git data...")
    diffs = extract_git_data(args.repo, args.author, args.date, start_date=args.start_date, end_date=args.end_date)
    if not diffs:
        print("No diffs found for the given date and author.")
        exit(0)
    print("Summarizing diffs...")
    summaries = summarize_all_diffs(diffs, args.model)
    print("Generating daily summary...")
    report = generate(summaries, args.author, args.date, args.model)
    print("Done!")
    with open("daily_summary.md", "w") as f:
        f.write(report)

def check_env():
    if not os.environ.get("OPENAI_API_KEY"):
        sys.stderr.write("Error: OPENAI_API_KEY environment variable is not set. Please set the variable and try again.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
