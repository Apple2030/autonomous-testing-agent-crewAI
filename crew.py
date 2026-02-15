from crewai import Crew, Task
from agents.requirement_agent import requirement_agent
from agents.test_design_agent import test_design_agent
from agents.playwright_generator_agent import playwright_generator_agent

def create_crew(story_data):

    task1 = Task(
        description=f"Extract test scenarios from story: {story_data}",
        agent=requirement_agent
    )

    task2 = Task(
        description="Design detailed test cases",
        agent=test_design_agent
    )

    task3 = Task(
        description="Generate Playwright TypeScript test script",
        agent=playwright_generator_agent
    )

    crew = Crew(
        agents=[requirement_agent, test_design_agent, playwright_generator_agent],
        tasks=[task1, task2, task3],
        verbose=True
    )

    return crew
