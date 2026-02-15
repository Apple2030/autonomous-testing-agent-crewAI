from jira import JIRA
from config import JIRA_URL, JIRA_USER, JIRA_TOKEN

class JiraClient:
    def __init__(self):
        self.client = JIRA(
            server=JIRA_URL,
            basic_auth=(JIRA_USER, JIRA_TOKEN)
        )

    def get_story(self, issue_key):
        issue = self.client.issue(issue_key)
        return {
            "summary": issue.fields.summary,
            "description": issue.fields.description
        }

    def create_bug(self, project_key, summary, description):
        self.client.create_issue(
            project=project_key,
            summary=summary,
            description=description,
            issuetype={"name": "Bug"}
        )
