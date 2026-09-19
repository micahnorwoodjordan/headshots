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
turn this image of me into a professional headshot.
i should be outside in front of a cactus with a slight smile.
preserve all of my facial and hair features
'''

pipeline = AutoPipelineForImage2Image.from_pretrained("Qwen/Qwen-Image-Edit-2509", dtype=torch.bfloat16, device="cpu")
pipeline.load_lora_weights("dx8152/Qwen-Edit-2509-Multiple-angles")
pipeline.to("cuda")

print(pipeline.device)

image = pipeline(image=Image.open("artifacts/input/headshot.jpg"), prompt=PROMPT).images[0]
print(image)
print(dir(image))
image.save("artifacts/output/result.jpg")
