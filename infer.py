import os
from huggingface_hub import InferenceClient


client = InferenceClient(provider="fal-ai", api_key=os.environ["HF_TOKEN"])

with open("cat.png", "rb") as image_file:
   input_image = image_file.read()


image = client.image_to_image(input_image, prompt="Turn the cat into a tiger.", model="black-forest-labs/FLUX.2-klein-4B")
image.save('tiger.jpg')
