import requests
from dotenv_ import BASE_URL, GITHUB_TOKEN, GITHUB_USERNAME


# Function to create a repository
def create_repo(repo_name):
    url = f"{BASE_URL}/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False  # Public repository
    }
    response = requests.post(url, headers=headers, json=data)
    return response


# Function to check if the repository exists
def repo_exists(repo_name):
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response = requests.get(url)
    return response.status_code == 200


# Function to delete a repository
def delete_repo(repo_name):
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code == 204
