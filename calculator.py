from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 20)

def button_click(number):
	digit = e.get()
	e.delete(0, END)
	e.insert(0, str(digit) + str(number))

def button_add():
	global first_num
	global math
	math = "addition"
	first_num = e.get()
	e.delete(0, END)

def button_mul():
	global first_num
	global math
	math = "multiplication"
	first_num = e.get()
	e.delete(0, END)

def button_sub():
	global first_num
	global math
	math = "subtraction"
	first_num = e.get()
	e.delete(0, END)

def button_div():
	global first_num
	global math
	math = "division"
	first_num = e.get()
	e.delete(0, END)

def button_equal():	
	sec_num = e.get()
	e.delete(0, END)
	if math == "addition":
		e.insert(0, int(first_num) + int(sec_num))
	if math == "multiplication":
		e.insert(0, int(first_num) * int(sec_num))
	if math == "subtraction":
		e.insert(0, int(first_num) - int(sec_num))
	if math == "division":
		e.insert(0, int(first_num) / int(sec_num))

def clear():
	e.delete(0, END)

	
#creating buttons
button_1 = Button(root, text = "1", height = 5, width = 10,command = lambda:button_click(1))
button_2 = Button(root, text = "2", height = 5, width = 10, command = lambda:button_click(2))
button_3 = Button(root, text = "3", height = 5, width = 10, command = lambda:button_click(3))
button_4 = Button(root, text = "4", height = 5, width = 10, command = lambda:button_click(4))
button_5 = Button(root, text = "5", height = 5, width = 10, command = lambda:button_click(5))
button_6 = Button(root, text = "6", height = 5, width = 10, command = lambda:button_click(6))
button_7 = Button(root, text = "7", height = 5, width = 10, command = lambda:button_click(7))
button_8 = Button(root, text = "8", height = 5, width = 10, command = lambda:button_click(8))
button_9 = Button(root, text = "9", height = 5, width = 10, command = lambda:button_click(9))
button_0 = Button(root, text = "0", height = 5, width = 10, command = lambda:button_click(0))

button_add = Button(root, text = "+", height = 5, width = 10, bg = "#A1CAE2", command = button_add)
button_mul = Button(root, text = "*", height = 5, width = 10, bg = "#A1CAE2", command = button_mul)
button_sub = Button(root, text = "-", height = 5, width = 10, bg = "#A1CAE2", command = button_sub)
button_div = Button(root, text = "/", height = 5, width = 10, bg = "#A1CAE2", command = button_div)
button_equal = Button(root, text = "=", height = 5, width = 10, bg = "#A1CAE2", command = button_equal)
button_clear = Button(root, text = "Clear", height = 5, width = 10, bg = "#A1CAE2", command = clear)

#placing buttons
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)

button_add.grid(row = 4, column = 1)
button_sub.grid(row = 1, column = 4)
button_mul.grid(row = 2, column = 4)
button_div.grid(row = 3, column = 4)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 4, column = 4)

root.mainloop()