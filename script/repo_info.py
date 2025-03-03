import requests
import sys


def fetch_latest_commit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch latest commit. {e}")
        sys.exit(1)

    print(f"{'='*50}\nLatest Commit Details\n{'='*50}")

    commits = response.json()
    latest_commit = commits[0]
    sha = latest_commit["sha"]
    message = latest_commit["commit"]["message"]
    author = latest_commit["commit"]["author"]["name"]
    date = latest_commit["commit"]["author"]["date"]
    print(
        f"Latest Commit sha: {sha}\n"
        f"Message: {message}\n"
        f"Author: {author}, Date: {date}\n"
    )


def fetch_issues(owner, repo, page_size):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {"state": "open", "per_page": page_size}
    issue_count = 0

    print(f"{'='*50}\nList of Issues\n{'='*50}")

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(
                f"Error: Unable to fetch issues. "
                f"Status code: {response.status_code}"
            )
            sys.exit(1)

        issues = response.json()
        if not issues:
            print("No open issues found")

        issue_count += len(issues)
        print(f"Fetching issues {issue_count - len(issues) + 1}-{issue_count}...")

        for issue in issues:
            print(f"Issue: {issue['title']}, Status: {issue['state']}")

        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break


def fetch_pull_requests(owner, repo, page_size):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {"state": "open", "per_page": page_size}
    pr_count = 0

    print(f"{'='*50}\nList of Pull Requests\n{'='*50}")

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(
                f"Error: Unable to fetch pull requests. "
                f"Status code: {response.status_code}"
            )
            sys.exit(1)

        pulls = response.json()
        if not pulls:
            print("No open pull requests found")

        pr_count += len(pulls)
        print(f"Fetching pull requests {pr_count - len(pulls) + 1}-{pr_count}...")

        for pr in pulls:
            print(f"Pull Request: {pr['title']}, Status: {pr['state']}")

        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break
