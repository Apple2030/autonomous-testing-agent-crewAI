from github import Github
from config import GITHUB_TOKEN, GITHUB_REPO

class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)
        self.repo = self.client.get_repo(GITHUB_REPO)

    def commit_file(self, file_path, content, branch="auto-tests"):
        try:
            self.repo.create_file(
                file_path,
                "Add autonomous test",
                content,
                branch=branch
            )
        except Exception:
            contents = self.repo.get_contents(file_path, ref=branch)
            self.repo.update_file(
                file_path,
                "Update autonomous test",
                content,
                contents.sha,
                branch=branch
            )

    def create_pull_request(self, title, body, head="auto-tests", base="main"):
        self.repo.create_pull(
            title=title,
            body=body,
            head=head,
            base=base
        )
