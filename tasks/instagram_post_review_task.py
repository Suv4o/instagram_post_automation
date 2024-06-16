from crewai import Task
from agents.instagram_post_review_agent import instagram_post_review_agent

instagram_post_review_task = Task(
    description=(
        "Review the Instagram post and ensure it is focused on the following {image} and its contents. "
        "Also, ensure that the caption does not exceed 2000 characters including hashtags."
    ),
    expected_output="A review report indicating whether the Instagram post meets the specified criteria.",
    agent=instagram_post_review_agent,
)
