## About
This Python script authenticates with your GitHub account, retrieves a list of all your repositories, and for each repository, fetches the most recent commits. It prints repository names along with their corresponding commit messages, authors, and timestamps in a readable format.

## Features
1. Authenticates using a GitHub personal access token

2. Fetches all your repositories (public and private)

3. Displays recent commits for each repository

4. Shows commit message, author, and timestamp in a readable format

## Setup and Run
1. Install required packages:

   pip install requests
2. Generate Github Personal Access Token

   Go to GitHub Settings > Developer settings > Personal access tokens.
3. Edit the script

   GITHUB_TOKEN = 'your_personal_access_token'
4. Run: python githubapi.py

<img width="623" alt="Screenshot 2025-06-12 at 12 54 39 PM" src="https://github.com/user-attachments/assets/3ad9e37d-72bb-47db-ba69-14888199f529" />
