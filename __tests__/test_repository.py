import pytest
import time
from repositories import create_repo, repo_exists, delete_repo


class TestGitHubAPI:
    
    def test_create_and_delete_repo(self):
        repo_name = "test-repo"
        
        # Create the repository
        response = create_repo(repo_name)
        assert response.status_code == 201
        
        # Adding a delay
        time.sleep(5)
        # Verify the repository was created
        assert repo_exists(repo_name) is True
        
        time.sleep(5)
        # Delete the repository
        assert delete_repo(repo_name) is True
