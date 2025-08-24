from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

sd_pipe = StableDiffusionPipeline.from_pretrained(
    "sd-legacy/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")

DEFAULT_NEGATIVE_PROMPT = (
    "blurry, low quality, bad anatomy, disfigured, poorly drawn, watermark, signature, distorted"
)

def generate_image_from_text(prompt: str, output_folder: str):
    image = sd_pipe(
        prompt, 
        negative_prompt=DEFAULT_NEGATIVE_PROMPT,
        guidance_scale=7.5
    ).images[0]
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(output_folder, filename)
    image.save(filepath)
    return filename
