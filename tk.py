from tkinter import *
root = Tk()
root.title("Calculator")

input1 = Entry(root, width = 45, borderwidth = 5)
input1.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# click and clear
def button_click(number):
	string = input1.get()
	input1.delete(0, END)
	input1.insert(0, str(string) + str(number))

def button_clear():
	input1.delete(0, END)

# add
def button_add():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "qushish"
	saving_number = int(take_number)
	input1.delete(0, END)

# minus
def button_minus():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "ayirish"
	saving_number = int(take_number)
	input1.delete(0, END)

# multiple
def button_multiple():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "ko'paytirish"
	saving_number = int(take_number)
	input1.delete(0, END)

# division
def button_division():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "bo'lish"
	saving_number = int(take_number)
	input1.delete(0,END)

# button_r
def button_r():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "qoldiq"
	saving_number = int(take_number)
	input1.delete(0, END)

# square
def button_square():
	take_number = input1.get()
	global saving_number
	global amal
	amal = "daraja"
	saving_number = int(take_number)
	input1.delete(0, END)

# equal
def button_equal():
	total = input1.get()
	input1.delete(0, END)
	if amal == "qushish":
		input1.insert(0, saving_number + int(total))
	if amal == "ayirish":
		input1.insert(0, saving_number - int(total))
	if amal == "ko'paytirish":
		input1.insert(0, saving_number * int(total))
	if amal == "bo'lish":
		input1.insert(0, saving_number / int(total))
	if amal == "qoldiq":
		input1.insert(0, saving_number / int(total))
	if amal == "daraja":
		input1.insert(0, saving_number ** int(total))


# buttons
button_7 = Button(root, text = "7", padx= 40, pady= 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx= 40, pady= 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx= 40, pady= 20, command = lambda: button_click(9))

button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
button_minus = Button(root, text = "-", padx = 40, pady = 20, command = button_minus)
button_equal = Button(root, text = "=", padx = 140, pady = 20, command = button_equal)
button_multiple = Button(root, text = "x", padx = 40, pady = 20, command = button_multiple)
button_division = Button(root, text = "/", padx = 40, pady = 20, command = button_division)
button_r = Button(root, text = "%", padx = 40, pady = 20, command = button_r)
button_square = Button(root, text = "**", padx = 40, pady = 20, command = button_square)
button_clear = Button(root, text = "clear", padx = 30, pady = 20, command = button_clear)


# rows and columns
button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)

button_4.grid(row = 6, column = 0)
button_5.grid(row = 6, column = 1)
button_6.grid(row = 6, column = 2)

button_1.grid(row = 9, column = 0)
button_2.grid(row = 9, column = 1)
button_3.grid(row = 9, column = 2)
button_0.grid(row = 12, column = 0)

button_add.grid(row = 3, column = 3)
button_minus.grid(row = 6, column = 3)
button_division.grid(row = 9, column = 3)
button_multiple.grid(row = 12, column = 3)
button_square.grid(row = 12, column = 1)
button_r.grid(row = 12, column = 2)
button_equal.grid(row = 15, column = 1, columnspan = 3)
button_clear.grid(row = 15, column = 0)

root.mainloop()