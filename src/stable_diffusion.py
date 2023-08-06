# As from https://platform.stability.ai/sandbox/text-to-image
import os
import base64
import requests
from dotenv import load_dotenv


API_KEY_NAME = "stableai.api_key"


class StableDiffusion:

	def __init__(self, illustration_folder_path: str) -> None:
		load_dotenv()
		api_key = os.environ.get(API_KEY_NAME)
		if api_key is None:
			raise Exception(f'"{API_KEY_NAME}" is not set in .env file!')
		self._api_key = api_key
		self._illustration_folder_path = illustration_folder_path

	def createIllustration(self, question: str, id: str) -> None:

		url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-beta-v2-2-2/text-to-image"

		body = {
			"width": 512,
			"height": 512,
			"steps": 50,
			"seed": 0,
			"cfg_scale": 7,
			"samples": 1,
			"style_preset": "enhance",
			"text_prompts": [
				{
					"text": f"For a quiz with different questions I want an illustration \
							fitting to the current question. The illustration should be \
							drawn in a cartoon style. Use only the colors white, blue, grey \
							and violet. The current question is: {question}",
					"weight": 1
				}
			],
		}

		headers = {
			"Accept": "application/json",
			"Content-Type": "application/json",
			"Authorization": f"{self._api_key}",
		}

		response = requests.post(
			url,
			headers=headers,
			json=body,
		)

		if response.status_code != 200:
			raise Exception("Non-200 response: " + str(response.text))

		data = response.json()

		for _, image in enumerate(data["artifacts"]):
			# seed = image['seed']
			with open(f"{self._illustration_folder_path}/illustration_{id}.png", "wb") as f:
				f.write(base64.b64decode(image["base64"]))


def main() -> None:
	question = "Was Christopher Columbus the first European to discover the Americas?"
	print(f"Creating image for question: {question}")
	project_root = "."
	id = "test"
	stable_diffusion = StableDiffusion(project_root)
	stable_diffusion.createIllustration(question, id)


if __name__ == "__main__":
	main()
