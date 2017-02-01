#(* v *)
from PIL import Image

im = Image.open("1.png")
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((0, 0))
width, height = im.size

print r, g, b
print width, height

rgb = []