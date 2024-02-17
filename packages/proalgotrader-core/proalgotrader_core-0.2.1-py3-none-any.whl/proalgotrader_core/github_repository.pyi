from pydantic import BaseModel

class GithubRepository(BaseModel):
    id: int
    repository_owner: str
    repository_name: str
    repository_full_name: str
    repository_ssh_url: str
    github_account_id: int
