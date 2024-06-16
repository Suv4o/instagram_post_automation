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

location_research_agent = Agent(
    role="Location Research Analyst",
    goal="To research and provide detailed information about the location where the image was taken."
    "The image is titled {image_title}.",
    memory=True,
    tools=[search_tool, web_rag_tool],
    verbose=False,
    backstory=(
        "I am a location research analyst, skilled in researching locations"
        "based on the information provided in the image title."
    ),
)
