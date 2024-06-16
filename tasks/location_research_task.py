from crewai import Task
from agents.location_research_agent import location_research_agent

location_research_task = Task(
    description=(
        "Research and provide detailed information about the location where the image titled {image_title} was taken."
    ),
    expected_output="Detailed information about the location where the image titled {image_title} was taken.",
    agent=location_research_agent,
)
