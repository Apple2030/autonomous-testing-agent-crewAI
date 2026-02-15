from crewai import Agent

test_design_agent = Agent(
    role="Test Designer",
    goal="Create positive, negative, and edge test cases",
    backstory="Senior QA architect specializing in boundary testing."
)
