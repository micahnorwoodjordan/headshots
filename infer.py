import os
from huggingface_hub import InferenceClient


REPO_ID = "black-forest-labs/FLUX.2-klein-4B"
INPUT_PATH = "artifacts/input/cat.png"
OUTPUT_PATH = "artifacts/output/tiger.jpg"


client = InferenceClient(provider="fal-ai", api_key=os.environ["HF_TOKEN"])

with open(INPUT_PATH, "rb") as image_file:
   input_image = image_file.read()


image = client.image_to_image(input_image, prompt="Turn the cat into a tiger.", model=REPO_ID)

if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

image.save(OUTPUT_PATH)
