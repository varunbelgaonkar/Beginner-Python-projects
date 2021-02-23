from tkinter import *
import sqlite3

root = Tk()
root.title("Employee Data")
root.geometry("400x400")


#cxreating a databse
#conn = sqlite3.connect("employee.db")

#creating curser
#c = conn.cursor()

#creating table
#c.execute("""CREATE TABLE employees(
#				emp_id integer,
#				first_name text,
#				last_name text,
#				age integer,
#				pay real
#				)""")
#

#inserting values in database
def insert_data():
	conn = sqlite3.connect("employee.db")
	c = conn.cursor()
	c.execute("INSERT INTO employees VALUES(:emp_id,:first_name,:last_name,:age,:pay)",{
					'emp_id':emp_id_t.get(),
					'first_name':first_name_t.get(),
					'last_name':last_name_t.get(),
					'age':age_t.get(),
					'pay':pay_t.get()})
	conn.commit()

	emp_id_t.delete(0, END)
	first_name_t.delete(0, END)
	last_name_t.delete(0, END)
	age_t.delete(0, END)
	pay_t.delete(0, END)

	conn.close()	

def show():
	conn = sqlite3.connect("employee.db")
	c = conn.cursor()
	c.execute("SELECT * FROM employees")
	data =  c.fetchall()
	print(data)
	record = ""
	for records in data:
		record += str(records) + "\n"
	label = Label(root, text = record, padx = 10, pady = 10)
	label.grid(row = 9, column = 1, columnspan = 3)
	conn.close()

##employee details widget labels
emp_id = Label(root, text="Emp_ID", padx = 10, pady = 10)
first_name = Label(root, text="Name", padx = 10, pady = 10)
last_name = Label(root, text="Last", padx = 10, pady = 10)
age = Label(root, text="Age", padx = 10, pady = 10)
pay = Label(root, text="Pay", padx = 10, pady = 10)

#textbox
emp_id_t = Entry(root, width = 30)
first_name_t = Entry(root, width = 30)
last_name_t = Entry(root, width = 30)
age_t = Entry(root, width = 30)
pay_t = Entry(root, width = 30)

#submit button
submit_btn = Button(root, text = "Add Record", padx = 50, pady = 20, command = insert_data)
submit_btn.grid(row = 5, column = 1, columnspan = 3)
#exit button
exit_btn = Button(root, text = "Exit", padx = 71, pady = 20, command = root.quit)
exit_btn.grid(row = 7, column = 1, columnspan = 3)
#query button
query_btn = Button(root, text = "Query", padx = 65, pady = 20, command = show)
query_btn.grid(row = 6, column=1, columnspan = 3)

#placing labels
emp_id.grid(row=0, column = 0)
first_name.grid(row=1, column = 0)
last_name.grid(row=2, column = 0)
age.grid(row=3, column = 0)
pay.grid(row=4, column = 0)

#placing textboxes
emp_id_t.grid(row=0, column = 1, columnspan = 3)
first_name_t.grid(row=1, column = 1, columnspan = 3)
last_name_t.grid(row=2, column = 1, columnspan = 3)
age_t.grid(row=3, column = 1, columnspan = 3)
pay_t.grid(row=4, column = 1, columnspan = 3)

root.mainloop()