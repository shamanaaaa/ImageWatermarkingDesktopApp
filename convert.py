import random
from PIL import Image, ImageDraw, ImageFont


def image_converter(image, dst_folder, count, size):
    # Opening Image & Creating New Text Layer
    img = Image.open(f'{image}').convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating Text
    text = "Mária Domanová\nneupravené zábery"
    font = ImageFont.truetype("ubuntu.ttf", size)

    # Creating Draw Object
    draw = ImageDraw.Draw(txt)

    # Positioning of Text
    width, height = img.size

    # Loop for Multiple Watermarks
    y = 200
    for i in range(count):
        x = (width/2 - 100)
        y += random.randrange(0, int(height / 16), 19) + random.randint(0, 100)
        draw.text((x, y), text, fill=(255, 255, 255, 75), font=font)

    # Combining both layers and saving new image
    watermarked = Image.alpha_composite(img, txt)
    img_split = image.split("/")[-1]
    watermarked.save(f'{dst_folder}/{img_split}.png')

