from crewai import Agent
from utils import analyse_image
from dotenv import dotenv_values
import os

env = dotenv_values(".env")

api_key = env["OPENAI_API_KEY"]
model_key = env["OPENAI_MODEL_NAME"]
serper_key = env["SERPER_API_KEY"]

os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_MODEL_NAME"] = model_key
os.environ["SERPER_API_KEY"] = serper_key


instagram_post_agent = Agent(
    role="Instagram Post Writer",
    goal="To create engaging Instagram posts based on the provided {image}."
    "The post should be engaging and interesting, include relevant emojis, and have a personal touch."
    "The caption should not exceed 2000 characters including hashtags."
    "The post should have a personal touch, for example using 'I' in a context 'I took this image...' or 'I visited this place...'.",
    memory=True,
    tools=[analyse_image],
    verbose=False,
    backstory=(
        "I am a computer program that has been trained to create engaging Instagram posts"
        "based on the provided image."
    ),
)
