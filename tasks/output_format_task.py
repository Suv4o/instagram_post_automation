from crewai import Task
from agents.output_format_agent import output_format_agent

output_format_task = Task(
    description=(
        "Format the final output to ensure it contains only the caption of the Instagram post. Noting else should be included. Exclude any titles or markdowns."
    ),
    expected_output="only the caption of the Instagram post.",
    agent=output_format_agent,
)
