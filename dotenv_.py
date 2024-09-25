"""variables it save data from the env"""
import os
import dotenv
dotenv.load_dotenv()
# GitHub token for authentication
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", '')
# GitHub API base URL
BASE_URL = os.getenv("BASE_URL", '')

# GitHub user-name
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", '')
