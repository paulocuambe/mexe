from PIL import Image, ImageFilter


im = Image.open("img1.jpg")

angle = 90
out = im.rotate(angle)
out.thumbnail((250, 250))
out.save(f"img1-angle{angle}.jpg")
