from agents.instagram_post_agent import instagram_post_agent
from agents.hashtag_research_agent import hashtag_research_agent
from agents.location_research_agent import location_research_agent
from agents.instagram_post_review_agent import instagram_post_review_agent
from agents.output_format_agent import output_format_agent
from tasks.instagram_post_task import instagram_post_task
from tasks.hashtag_research_task import hashtag_research_task
from tasks.location_research_task import location_research_task
from tasks.instagram_post_review_task import instagram_post_review_task
from tasks.output_format_task import output_format_task
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import dotenv_values


env = dotenv_values(".env")
model_key = env["OPENAI_MODEL_NAME"]


crew = Crew(
    agents=[
        instagram_post_agent,
        hashtag_research_agent,
        location_research_agent,
        instagram_post_review_agent,
        output_format_agent,
    ],
    tasks=[
        instagram_post_task,
        hashtag_research_task,
        location_research_task,
        instagram_post_review_task,
        output_format_task,
    ],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model=model_key),
    full_output=False,
    verbose=False,
    memory=True,
    max_rpm=100,
)
