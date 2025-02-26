from repo_info import *

if __name__ == "__main__":
    OWNER = "jenkinsci"
    REPO = "jenkins"
    PAGE_SIZE = 20

    fetch_latest_commit(OWNER, REPO)
    fetch_issues(OWNER, REPO, PAGE_SIZE)
    fetch_pull_requests(OWNER, REPO, PAGE_SIZE)