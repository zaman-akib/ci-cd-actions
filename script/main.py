from repo_info import *

if __name__ == "__main__":
    OWNER = "jenkinsci"
    REPO = "jenkins"
    fetch_latest_commit(OWNER, REPO)
    fetch_issues(OWNER, REPO)
    fetch_pull_requests(OWNER, REPO)