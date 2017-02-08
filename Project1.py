#(* v *)
from PIL import Image

img1 = Image.open("1.png")#opens image file so that the values can be obtained
rgb_img1 = img1.convert('RGB')#converts image data into RGB values
#Repeated for all 9 images
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
#old code that is not being used

newRGB = []#An empty list to store all of the RGB values for the new list

width, height = img1.size#size returns a tuple of width and height in that order
#By setting two variables to the image size in this order, the first variable
#will be the width and the second will be the height
dimensions = img1.size#Gets the image size(width and height) as a tuple in one
#variable to be used later
for y in range(height):
     for x in range(width):#nested for loop that goes through the x and y values
     #to get every coordinate 
          r = []#seperate empty list for the rgb values so that the final list
          #can have the median from each of the values
          g = []
          b = []
          r1, g1, b1 = rgb_img1.getpixel((x, y))#gets the coordinates of every
          #pixel for three different variables set up so that the red, blue, 
          #and green values are stored seperately
          r.append(r1)#adds the red value of image1 to the red list
          g.append(g1)#adds the green value of image1 to the green list
          b.append(b1)#adds the blue value of image1 to the blue list
          #repeats for every image
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
          
          r = sorted(r)#sorts every r value so that it is ordered from smallest 
          #to largest
          g = sorted(g)#sorts green values
          b = sorted(b)#sorts blue values
          
          length = len(r) / 2 #makes a variable named length the value of the
          #amount of items in the r list divided by two, since it is an integer,
          #9/2 turns into 4 which is the middle value
          newRGB.append((r[length], g[length], b[length]))#adds the red, 
          # green, and blue pixel values from their respective list at the spot in
          # the middle of the images so that it is the median of all of the values
          # to the list outside of the loop to make a list of median rgb values 
          # for the new image

lastImg = Image.new("RGB", dimensions)#variable for the final picture that is 
#made with rgb values and has the width and length of the other images since the
#variable dimensions is a tuple obtained from the first image
lastImg.putdata(newRGB)#puts the information from the newRGB list to give put 
#all of the median rgb values together and make the new image
lastImg.save("final.png")#saves tbe new image created to the file named
#"final.png" which can then be opened to see the new image made up of the 
#median values of all of the previous images