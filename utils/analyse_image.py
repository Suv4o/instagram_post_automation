import io, base64, requests
from crewai_tools import tool
from PIL import Image
from dotenv import dotenv_values

env = dotenv_values(".env")

model_key = env["OPENAI_MODEL_NAME"]
api_key = env["OPENAI_API_KEY"]


def encode_image(image_path, max_size=(2000, 2000)):
    with Image.open(image_path) as img:
        img.thumbnail(max_size)

        byte_arr = io.BytesIO()
        img.save(byte_arr, format="JPEG")

        return base64.b64encode(byte_arr.getvalue()).decode("utf-8")


@tool("Analyse Image")
def analyse_image(image_path: str) -> str:
    """Analyse the image and provide a detailed description on what is in the image"""
    base64_image = encode_image(image_path)
    local_image = f"data:image/jpeg;base64,{base64_image}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "model": model_key,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": local_image},
                    },
                ],
            }
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    response_json = response.json()

    choices = response_json["choices"]
    message = choices[0]["message"]
    content = message["content"]

    return content
