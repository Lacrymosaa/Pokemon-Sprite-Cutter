import os
from PIL import Image

source_folder = 'Front'
destination_folder = 'Output'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    if filename.endswith('.png'):

        img_path = os.path.join(source_folder, filename)

        img = Image.open(img_path)

        sprite_height = img.height  
        sprite_width = sprite_height  
        sprite = img.crop((0, 0, sprite_width, sprite_height))

        sprite.save(os.path.join(destination_folder, filename))

print("Done!")
