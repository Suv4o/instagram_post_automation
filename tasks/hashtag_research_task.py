from crewai import Task
from agents.hashtag_research_agent import hashtag_research_agent

hashtag_research_task = Task(
    description="Analyse the hashtags and provide suggestions for improvement.",
    expected_output="A list of hashtags with suggestions for improvement.",
    agent=hashtag_research_agent,
)
