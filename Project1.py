#(* v *)
from PIL import Image

img1 = Image.open("1.png")
rgb_img1 = img1.convert('RGB')

img2 = Image.open("2.png")
rgb_img2 = img2.convert('RGB')

img3 = Image.open("3.png")
rgb_img3 = img3.convert('RGB')

img4 = Image.open("4.png")
rgb_img4 = img4.convert('RGB')

img5 = Image.open("5.png")
rgb_img5 = img5.convert('RGB')

img6 = Image.open("6.png")
rgb_img6 = img6.convert('RGB')

img7 = Image.open("7.png")
rgb_img7 = img7.convert('RGB')

img8 = Image.open("8.png")
rgb_img8 = img8.convert('RGB')

img9 = Image.open("9.png")
rgb_img9 = img9.convert('RGB')
#r, g, b = rgb_im.getpixel((0, 0))
#print r, g, b
#print width, height
newRGB = []

width, height = img1.size
dimensions = img1.size
for y in range(height):
     for x in range(width):
          r = []
          g = []
          b = []
          r1, g1, b1 = rgb_img1.getpixel((x, y))
          r.append(r1)
          g.append(g1)
          b.append(b1)
          r2, g2, b2 = rgb_img2.getpixel((x, y))
          r.append(r2)
          g.append(g2)
          b.append(b2)
          r3, g3, b3 = rgb_img3.getpixel((x, y))
          r.append(r3)
          g.append(g3)
          b.append(b3)
          r4, g4, b4 = rgb_img4.getpixel((x, y))
          r.append(r4)
          g.append(g4)
          b.append(b4)
          r5, g5, b5 = rgb_img5.getpixel((x, y))
          r.append(r5)
          g.append(g5)
          b.append(b5)
          r6, g6, b6 = rgb_img6.getpixel((x, y))
          r.append(r6)
          g.append(g6)
          b.append(b6)
          r7, g7, b7 = rgb_img7.getpixel((x, y))
          r.append(r7)
          g.append(g7)
          b.append(b7)
          r8, g8, b8 = rgb_img8.getpixel((x, y))
          r.append(r8)
          g.append(g8)
          b.append(b8)
          r9, g9, b9 = rgb_img9.getpixel((x, y))
          r.append(r9)
          g.append(g9)
          b.append(b9)
          
          r = sorted(r)
          g = sorted(g)
          b = sorted(b)
          
          length = len(r) / 2
          newRGB.append((r[length], g[length], b[length]))

lastImg = Image.new("RGB", dimensions)
lastImg.putdata(newRGB)
lastImg.save("final.png")