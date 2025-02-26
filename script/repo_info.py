import requests
import sys

def fetch_latest_commit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
        sys.exit(1)

    print(f"{'='*50}\nLatest Commit Details\n{'='*50}")

    commits = response.json()
    latest_commit = commits[0]
    sha = latest_commit['sha']
    message = latest_commit['commit']['message']
    author = latest_commit['commit']['author']['name']
    date = latest_commit['commit']['author']['date']
    print(f"Latest Commit sha: {sha}\nMessage: {message}\nAuthor: {author}, Date: {date}\n")

def fetch_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {'state': 'open', 'per_page': 10}

    print(f"{'='*50}\nList of Issues\n{'='*50}")

    while url:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error: Unable to fetch issues. Status code: {response.status_code}")
            sys.exit(1)

        issues = response.json()
        for issue in issues:
            print(f"Issue: {issue['title']}, Status: {issue['state']}")

        url = response.links.get('next', {}).get('url')

def fetch_pull_requests(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {'state': 'open', 'per_page': 10}

    print(f"{'='*50}\nList of Pull Requests\n{'='*50}")

    while url:
     response = requests.get(url, params=params)
     if response.status_code != 200:
         print(f"Error: Unable to fetch pull requests. Status code: {response.status_code}")
         sys.exit(1)

     pulls = response.json()
     for pr in pulls:
         print(f"Pull Request: {pr['title']}, Status: {pr['state']}")

     url = response.links.get('next', {}).get('url')