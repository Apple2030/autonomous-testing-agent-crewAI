from crewai import Agent

playwright_generator_agent = Agent(
    role="Playwright Automation Engineer",
    goal="Generate executable Playwright TypeScript test scripts",
    backstory="Expert in modern browser automation using Playwright."
)
