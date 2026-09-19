"""
this script is a stub for utiliing diffusion models to generate professional headhsots based off of an input image.
these underlying models seem to be extremely powerful and can generate very high quality images.

the caveat is that the hardware required for speedy image generation is very expensive
"""
from PIL import Image
import torch
from diffusers import AutoPipelineForImage2Image


print("CUDA:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))


PROMPT = '''
turn this image of me into a professional headshot. preserve all of my facial and hair features. i should be:

- outside
- in front of a cactus
- slightly smiling
- facing 20 degrees to the left of the camera
'''

pipeline = AutoPipelineForImage2Image.from_pretrained("Qwen/Qwen-Image-Edit-2509", dtype=torch.bfloat16, device="cpu")
pipeline.load_lora_weights("dx8152/Qwen-Edit-2509-Multiple-angles")
pipeline.to("cuda")

print(pipeline.device)

image = pipeline(image=Image.open("artifacts/input/headshot.jpg"), prompt=PROMPT).images[0]
image.save("artifacts/output/result.jpg")
