import torch
from PIL import Image
from diffusers import StableDiffusionInstructPix2PixPipeline
import os
import uuid

edit_pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
    "timbrooks/instruct-pix2pix", torch_dtype=torch.float16
).to("cuda")

def edit_image_with_prompt(input_image: Image.Image, prompt: str, output_folder: str):
    edited_image = edit_pipe(prompt=prompt, image=input_image).images[0]
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(output_folder, filename)
    edited_image.save(filepath)
    return filename
