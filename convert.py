import random
from PIL import Image, ImageDraw, ImageFont


def image_converter(image, dst_folder, count, size):
    # Opening Image & Creating New Text Layer
    img = Image.open(f'{image}').convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating Text
    # text = "Mária Domanová\nneupravené zábery"
    text = "X"
    font = ImageFont.truetype("ubuntu.ttf", size)

    # Creating Draw Object
    draw = ImageDraw.Draw(txt)

    # Positioning of Text
    width, height = img.size

    # Loop for Multiple Watermarks
    # y_var = height / count
    # for i in range(count):
    #     x = (width / 2 - 200)
    #     y = y_var * i + 50
    #     draw.text((x, y), text, fill=(255, 255, 255, 35), font=font)
    if height == 900:
        x = -20
        y = -80
    else:
        x = 120
        y = -210

    draw.text((x, y), text, fill=(255, 255, 255, 85), font=font)

    # Combining both layers and saving new image
    watermarked = Image.alpha_composite(img, txt)
    img_split = image.split("/")[-1]
    watermarked.save(f'{dst_folder}/{img_split}.png')
