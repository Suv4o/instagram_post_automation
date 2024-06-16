from crewai import Task
from agents.instagram_post_agent import instagram_post_agent

instagram_post_task = Task(
    description=(
        "Compose an engaging Instagram post using the following image {image}"
    ),
    expected_output="An Instagram post using the following image {image}."
    "The post should be engaging and interesting."
    "Should include emojis where appropriate to make the post more fun and engaging."
    "And also include relevant hashtags to increase the reach of the post."
    "The caption should have a personal touch, for example using 'I' in a context 'I took this image...' or 'I visited this place...'.",
    agent=instagram_post_agent,
)
