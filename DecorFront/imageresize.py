import PIL
from PIL import Image


def image_resize(path):
    img = Image.open(path)
    img = img.resize((800, 600), PIL.Image.ANTIALIAS)
    img.save(path)


def logo_resize(path):
    img = Image.open(path)
    img = img.resize((200, 200), PIL.Image.ANTIALIAS)
    img.save(path)
