import requests

# Configuration
GITHUB_TOKEN = 'your_personal_access_token'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}
COMMITS_PER_REPO = 5  # Number of recent commits to fetch per repository

def get_all_repos():
    repos = []
    page = 1
    while True:
        response = requests.get(
            'https://api.github.com/user/repos',
            headers=HEADERS,
            params={'per_page': 100, 'page': page, 'affiliation': 'owner'}
        )
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def get_recent_commits(owner, repo_name):
    response = requests.get(
        f'https://api.github.com/repos/{owner}/{repo_name}/commits',
        headers=HEADERS,
        params={'per_page': COMMITS_PER_REPO}
    )
    response.raise_for_status()
    return response.json()

def main():
    repos = get_all_repos()
    
    for repo in repos:
        owner = repo['owner']['login']
        repo_name = repo['name']
        print(f"\nRepository: {repo_name} ({repo['html_url']})")
        print(f"Description: {repo['description'] or 'No description'}")
        print(f"Default Branch: {repo['default_branch']}")
        
        try:
            commits = get_recent_commits(owner, repo_name)
            if not commits:
                print("  No commits found")
                continue
                
            for commit in commits:
                commit_data = commit['commit']
                author = commit_data['author']['name']
                date = commit_data['author']['date']
                message = commit_data['message'].replace('\n', ' ')
                print(f"\n  Commit: {message}")
                print(f"  Author: {author}")
                print(f"  Date: {date}")
                
        except requests.exceptions.HTTPError as e:
            print(f"  Error retrieving commits: {e}")

if __name__ == "__main__":
    main()
