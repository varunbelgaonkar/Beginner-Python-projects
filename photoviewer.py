#importing libraries
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Photoviewer")

image_0 = ImageTk.PhotoImage(Image.open("Figure_0.png"))
image_1 = ImageTk.PhotoImage(Image.open("Figure_1.png"))
image_2 = ImageTk.PhotoImage(Image.open("Figure_2.png"))
image_3 = ImageTk.PhotoImage(Image.open("Figure_3.png"))
images = [image_0, image_1, image_2, image_3]

def next_image(num):	
	global label_img
	global button_next
	global button_back
	label_img.grid_forget()
	label_img = Label(root, image = images[num-1])
	label_img.grid(row = 0, column = 0, columnspan = 3)
	button_next = Button(root, text = "Next", height = 5, 
						width = 15, command = lambda : next_image(num + 1))
	button_back = Button(root, text = "Previous", height = 5, 
						width = 15, command = lambda : prev_image(num - 1))
	if num == 4:
		button_next = Button(root, text = "Next", height = 5, width = 15, 
							state = DISABLED)
	button_next.grid(row = 1, column = 2)
	button_back.grid(row = 1, column = 0)

def prev_image(num):
	global label_img
	global button_next
	global button_back
	label_img.grid_forget()
	label_img = Label(root, image = images[num-1])
	label_img.grid(row = 0, column = 0, columnspan = 3)
	button_next = Button(root, text = "Next", height = 5, 
						width = 15, command = lambda : next_image(num + 1))
	button_back = Button(root, text = "Previous", height = 5, 
						width = 15, command = lambda : prev_image(num - 1))
	button_next.grid(row = 1, column = 2)
	button_back.grid(row = 1, column = 0)
	if num == 1:
		button_back = Button(root, text = "Previous", height = 5, width = 15, 
							state = DISABLED)
	button_next.grid(row = 1, column = 2)
	button_back.grid(row = 1, column = 0)


label_img = Label(root, image = image_0)

button_next = Button(root, text = "Next", height = 5, 
					width = 15, command = lambda : next_image(1))
button_back = Button(root, text = "Previous", height = 5, 
					width = 15, state = DISABLED)
button_exit = Button(root, text = "Exit", height = 5, 
					width = 15, command = root.quit)

label_img.grid(row = 0, column = 0, columnspan = 3)
button_next.grid(row = 1, column = 2,)
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)

root.mainloop() 