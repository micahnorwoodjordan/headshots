import torch
from diffusers import Flux2KleinPipeline


REPO_ID = "black-forest-labs/FLUX.2-klein-4B"
DEVICE = "cuda"
DTYPE = torch.bfloat16
OUTPUT_PATH = "flux-klein.png"

pipe = Flux2KleinPipeline.from_pretrained(REPO_ID, torch_dtype=DTYPE)
pipe.enable_model_cpu_offload()  # save some VRAM by offloading the model to CPU

prompt = "A cat holding a sign that says hello world"
image = pipe(
    prompt=prompt,
    height=1024,
    width=1024,
    guidance_scale=1.0,
    num_inference_steps=4,
    generator=torch.Generator(device=DEVICE).manual_seed(0)
).images[0]

image.save(OUTPUT_PATH)
