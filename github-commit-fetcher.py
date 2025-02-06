import requests
import sys

def fetch_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
        sys.exit(1)
    
    commits = response.json()
    
    for commit in commits:
        sha = commit['sha']
        message = commit['commit']['message']
        author = commit['commit']['author']['name']
        date = commit['commit']['author']['date']
        print(f"Commit sha: {sha}\nMessage: {message}\nAuthor: {author}, Date: {date}\n{'='*50}")

if __name__ == "__main__":
    OWNER = "jenkinsci"
    REPO = "blackduck-security-scan-plugin"
    fetch_commits(OWNER, REPO)