import os, random, sys


sys.path.append("..")


def choose_random_image():
    image_dir = "./images"
    images = os.listdir(image_dir)
    image_name = random.choice(images)
    image_path = os.path.join(image_dir, image_name)
    return image_path
