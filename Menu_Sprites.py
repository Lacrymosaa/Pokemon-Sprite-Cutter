from PIL import Image
import os

input_folder = 'Icons'
output_folder = './output'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)

        img = Image.open(input_path)

        width, height = img.size

        left_half = img.crop((0, 0, width // 2, height))

        output_path = os.path.join(output_folder, filename)

        left_half.save(output_path)

print("Done!")
