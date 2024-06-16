import os
from utils import choose_random_image, post_on_instagram
from crew.crew import crew


image_name = choose_random_image()
image_path = os.path.abspath(image_name)


result = crew.kickoff(
    inputs={
        "image": image_name,
        "image_title": image_name.split(".")[0],
    }
)


post_on_instagram(image_path, result)
