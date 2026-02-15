from crewai import Agent

requirement_agent = Agent(
    role="Requirement Analyst",
    goal="Extract structured test scenarios from JIRA story",
    backstory="Expert QA analyst converting requirements into test scenarios."
)