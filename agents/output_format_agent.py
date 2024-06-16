from crewai import Agent
from dotenv import dotenv_values
import os

env = dotenv_values(".env")

api_key = env["OPENAI_API_KEY"]
model_key = env["OPENAI_MODEL_NAME"]
serper_key = env["SERPER_API_KEY"]

os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_MODEL_NAME"] = model_key
os.environ["SERPER_API_KEY"] = serper_key

output_format_agent = Agent(
    role="Output Formatter",
    goal="To ensure the final output contains only the caption of the Instagram post"
    "and does not include any titles or markdowns.",
    memory=True,
    verbose=False,
    backstory=(
        "I am a computer program that has been trained to format text outputs"
        "and ensure they meet the specified format."
    ),
)
