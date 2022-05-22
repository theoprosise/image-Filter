

from PIL import Image
import os

# Deletes old created images if they exist
# "StudentWork" is an example directory
images = ["StudentWork/combinedFilters.jpg","StudentWork/filter1.jpg","StudentWork/filter2.jpg","StudentWork/filter3.jpg","StudentWork/gray.jpg"]
for i in images:
	if os.path.exists(i):
		os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image
img = Image.open('StudentWork/image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
	scale = mwidth
else:
	scale = mheight
if scale != 0:
	img = img.resize( (width // scale, height // scale) )

# Compression Filter
def comp():
	print("Code for compression")
	pixels = img.getdata()
	new_pixels = []
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		if location % 4 == 0:
			newr = r
			newg = g
			newb = b
		# Assign new red, green and blue components to pixel
		# # at that specific location
		new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
		location = location + 1
	# Creates a new image, the same size as the original 
	# using RGB value format
	newImage = Image.new("RGB", img.size)
	# Assigns the new pixel values to newImage
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage


# Inverse Filter

def filter1():
	print("Code for inverse")
	pixels = img.getdata()
	new_pixels = []
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		newr = 2*(255-r)
		newg = 2*(255-g)
		newb = 2*(255-b)
		new_pixels[location] = (newr, newg, newb)
		location = location + 1
	newImage = Image.new("RGB", img.size)
	# Assigns the new pixel values to newImage
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage

# Oldschool Filter

def filter2():
	print("Code for oldschool")
	# Creates an ImageCore Object from original image
	pixels = img.getdata()
	# Creates empty array to hold new pixel values
	new_pixels = []
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		newr = r
		newg = g
		newb = b
		if location % 2 == 0:
			newr = 0
			newg = 0
			newb = 0
		new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
		location = location + 1
	newImage = Image.new("RGB", img.size)
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage

# Compression filter with varied level of compression

def filter3(mag):
	print("Code for compression")
	print(mag)
	pixels = img.getdata()
	new_pixels = []	# a copy of that pixel to our new_pixels array
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		# Perform pixel manipulation and stores results
		# to a new red, green and blue components
		num = int(mag)
		if location % num == 0:
			newr = r
			newg = g
			newb = b
		new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
		location = location + 1
	newImage = Image.new("RGB", img.size)
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage

# Creates the four filter images and saves them to example files
a = comp()
a.save("StudentWork/comp.jpg")
b = filter1()
b.save("StudentWork/filter1.jpg")
c = filter2()
c.save("StudentWork/filter2.jpg")
#d = filter3()
mag1 = input("Enter compression magnitude: ")
d = filter3(mag1)
d.save("StudentWork/filter3.jpg")

# Image filter names for use below
f1 = "inverse"
f2 = "oldschool"
f3 = "compressionCustom"

# Apply multiple filters through prompts with the user
print("\nThe following prompt will ask you which filter to apply to the combined filter. It will keep asking until you answer 'none'.")
answer = input("\nWhich filter do you want me to apply?\n compression\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "compression" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
	answer = input("\nIncorrect filter, please enter:\n compression\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "compression" or answer == f1 or answer == f2 or answer == f3:
	if answer == "compression":
		img = comp()
	elif answer == f1:
		img = filter1()
	elif answer == f2:
		img = filter2()
	elif answer == f3:
		#mag1 = input("Enter magnitude: ")
		img = filter3(mag1)
	else:
		break
	print("Filter \"" + answer + "\" applied...")
	answer = input("\nWhich filter do you want me to apply next?\n compression\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
	while answer != "compression" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
		answer = input("\nIncorrect filter, please enter:\n compression\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

print("Combined filter being created...Done")

# Create the combined filter image and saves it to our files
img.save("StudentWork/combinedFilters.jpg")
