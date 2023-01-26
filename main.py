# this project is going to convert the jpeg images into png extension using PIL library.
# written by: Faisal Almasri.
# Date: 25/Jan/2023

from PIL import Image
from os import listdir, mkdir
from sys import argv

# Creating a folder to save all the converted images.

try:
    mkdir('converted_images')
except FileExistsError:
    print("You create the folder before :0.")

# for each image in directory images
for image_name in listdir('./images'):
    img = Image.open(f"./images/{image_name}")
    img.thumbnail((512, 512))  # to compress the size of the image with keeping the aspect ratio as possible.

    without_extension = image_name[:-4]  # will generate the image name without .jpg extension.
    try:
        img.save(fp=f"./converted_images/{without_extension}.{argv[1]}", format=argv[1])
    except IndexError:
        print("You didn't specify the required extension")
        break
