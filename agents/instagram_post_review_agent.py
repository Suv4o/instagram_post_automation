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

instagram_post_review_agent = Agent(
    role="Instagram Post Reviewer",
    goal="To review Instagram posts and ensure they are focused on the following {image} and its contents,"
    "and that the caption does not exceed 2000 characters including hashtags."
    "Also ensure that the post is engaging and interesting and has relevant emojis."
    "The post also needs to ensure has a personal touch, for example using 'I' in a context 'I took this image...' or 'I visited this place...'."
    "Make sure the post has Australian spelling and grammar.",
    memory=True,
    tools=[analyse_image],
    verbose=False,
    backstory=(
        "I am a computer program that has been trained to review Instagram posts"
        "and ensure they meet the specified criteria."
    ),
)
