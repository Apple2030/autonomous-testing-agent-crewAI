import os
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PLAYWRIGHT_BASE_URL = os.getenv("PLAYWRIGHT_BASE_URL", "https://example.com")
