from repo_info import fetch_latest_commit, fetch_issues, fetch_pull_requests

if __name__ == "__main__":
    OWNER = "jenkinsci"
    REPO = "jenkins"
    PAGE_SIZE = 20

    fetch_latest_commit(OWNER, REPO)
    fetch_issues(OWNER, REPO, PAGE_SIZE)
    fetch_pull_requests(OWNER, REPO, PAGE_SIZE)
