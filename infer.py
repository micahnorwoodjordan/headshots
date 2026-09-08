import os
from huggingface_hub import InferenceClient


INPUT_PATH = "artifacts/input/headshot.jpg"
OUTPUT_PATH = "artifacts/output/result.jpg"

REPO_ID = "dx8152/Qwen-Edit-2509-Multiple-angles"
INFERENCE_PROVIDER = 'wavespeed'

PROMPT = '''
turn this image of me into a professional headshot.
i should be outside in front of a cactus with a slight smile.
preserve all of my facial and hair features
'''


client = InferenceClient(provider=INFERENCE_PROVIDER, api_key=os.environ["HF_TOKEN"])

with open(INPUT_PATH, "rb") as image_file:
   input_image = image_file.read()


image = client.image_to_image(input_image, prompt=PROMPT, model=REPO_ID)

if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

image.save(OUTPUT_PATH)
