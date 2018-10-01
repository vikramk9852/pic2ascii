from tkinter import *
import os
from PIL import Image

#default values
ls = [111, 119, 143, 162];

def function1(val):
	ls[0] = int(val)

def function2(val):
	ls[1] = int(val)

def function3(val):
	ls[2] = int(val)

def function4(val):
	ls[3] = int(val)

def convert():
	img = Image.open('check.jpg')
	width, height = img.size
	first = open('convert.html', 'w')
	first.write('<pre style="font: 10px/5px monospace;">')	
	for i in range(0, height, 4):
		for j in range(0, width, 4):
			a, b, c= img.getpixel((j, i));
			if (a, b, c) <= (ls[0], ls[0], ls[0]):
				first.write('#')
			elif (a, b, c) <= (ls[1], ls[1], ls[1]):
				first.write('+')
			elif (a, b, c) <= (ls[2], ls[2], ls[2]):
				first.write("'")
			elif (a, b, c) <= (ls[3], ls[3], ls[3]):
				first.write('.')
			else:
				first.write(',')
		first.write('\n')
	first.write('</pre>')
	first.close()
	print(ls)

root = Tk()
root.title('pic2ascii')
root["bg"] = "#e6f2ff"

scale = Scale(orient='horizontal', from_=0, to=256, command=function1, length=256, label = "darker", activebackground = "#9933ff", bg = "#00802b")
scale.set(ls[0])
scale.pack()

scale = Scale(orient='horizontal', from_=0, to=256, command=function2, length=256, label = "medium", activebackground = "#9933ff", bg = "#00cc44")
scale.set(ls[1])
scale.pack()

scale = Scale(orient='horizontal', from_=0, to=256, command=function3, length=256, label = "medium", activebackground = "#9933ff", bg = "#33ff77")
scale.set(ls[2])
scale.pack()

scale = Scale(orient='horizontal', from_=0, to=256, command=function4, length=256, label = "lighter", activebackground = "#9933ff", bg = "#ccffdd")
scale.set(ls[3])
scale.pack()

Button(root, text='Convert', command=convert).pack()

root.mainloop()
