from PIL import Image, ImageFilter


im = Image.open("img1.jpg")

angle = 20

im = im.rotate(angle)
im.thumbnail((250, 250))
im.crop((10, 10, 10, 10))
im.save(f"img1-angle{angle}.jpg")
