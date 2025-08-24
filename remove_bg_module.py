from rembg import remove
from PIL import Image
import uuid
import os
def remove_background_from_image(input_image: Image.Image, output_folder: str):
    output_image = remove(input_image)
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(output_folder, filename)
    output_image.save(filepath)
    return filename
