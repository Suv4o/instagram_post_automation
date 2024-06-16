from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool
from dotenv import dotenv_values
import os

env = dotenv_values(".env")

api_key = env["OPENAI_API_KEY"]
model_key = env["OPENAI_MODEL_NAME"]
serper_key = env["SERPER_API_KEY"]

os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_MODEL_NAME"] = model_key
os.environ["SERPER_API_KEY"] = serper_key

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


hashtag_research_agent = Agent(
    role="Hashtag Research Analyst",
    goal="To review and analyse the effectiveness of hashtags used in social media posts"
    "and suggest improvements for better reach and engagement.",
    memory=True,
    tools=[search_tool, web_rag_tool],
    verbose=False,
    backstory=(
        "I am a hashtag guardian to review hashtags"
        "and provide suggestions for improvement."
    ),
)
