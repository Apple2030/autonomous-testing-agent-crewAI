from integrations.jira_client import JiraClient
from integrations.github_client import GitHubClient
from agents.execution_agent import ExecutionAgent
from agents.failure_analysis_agent import FailureAnalysisAgent
from crew import create_crew

PROJECT_KEY = "PROJ"
ISSUE_KEY = "PROJ-101"

def main():

    jira = JiraClient()
    github = GitHubClient()

    # Step 1: Fetch Story
    story = jira.get_story(ISSUE_KEY)

    # Step 2: Create Crew
    crew = create_crew(story)
    result = crew.kickoff()

    # Step 3: Save generated test
    test_content = result
    file_path = "tests/generated.spec.ts"

    github.commit_file(file_path, test_content)

    # Step 4: Execute tests
    executor = ExecutionAgent()
    results = executor.run_tests()

    # Step 5: Analyze failures
    analyzer = FailureAnalysisAgent()
    failures = analyzer.analyze(results)

    if failures:
        for failure in failures:
            jira.create_bug(
                PROJECT_KEY,
                summary=f"Auto Detected: {failure['title']}",
                description=str(failure['error'])
            )

    else:
        github.create_pull_request(
            title="Autonomous Test Update",
            body="Generated and validated by Autonomous Testing Agent"
        )

if __name__ == "__main__":
    main()
