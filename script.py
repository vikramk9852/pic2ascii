import os
from PIL import Image
os.chdir('d:')
img = Image.open('checkk.jpg')
width, height = img.size
first = open('convert.html', 'w')
first.write('<pre style="font: 10px/5px monospace;">')
#change loop incrementer for expected width and height
for i in range(0, height, 5):
	for j in range(0, width, 5):
		a, b, c= img.getpixel((j, i));#a, b, c, d for png image files
		if (a, b, c) <= (100, 100, 100):#change the parameters according to darkness of the image
			first.write('#')
		elif (a, b, c) <= (170, 170, 170):#change the parameters according to darkness of the image
			first.write('+')
		elif (a, b, c) <= (180, 180, 180):#change the parameters according to darkness of the image
			first.write("'")
		elif (a, b, c) <= (200, 200, 200):#change the parameters according to darkness of the image
			first.write('.')
		else:
			first.write(',')
	first.write('\n')
first.write('</pre>')
first.close()
