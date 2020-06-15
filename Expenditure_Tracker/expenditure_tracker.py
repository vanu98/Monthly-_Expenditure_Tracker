from tkinter import *
import sqlite3 as s
import datetime


person = ['Varnesh', 'Albus', 'Edmond','Nicolas']

root = Tk()
root.title('Calorie Tracker')
root.geometry('800x800')
title = Label(root,text='Monthly Expenditure Tracker', font=('times new roman', 35, 'bold'), fg='white', bg='black')
title.pack()
name = StringVar(root)
name_label = Label(root, text='Enter your name...',font=("arial", 16)).place(relx=0.4,rely=0.4)
entry_name = Entry(root, textvariable=name)
entry_name.place(relx=0.4, rely=0.5)
b = Button(root, text="submit", command=lambda: cond(name.get()))
b.place(relx=0.4,rely =0.6)

def cond(name):
	if name in person:
		L7 = Label(root,text='Name is already registered',font=("arial", 16)).place(relx=0.4,rely=0.7)
	else:
		person.append(name)
		window1()
def window1():
	wind = Toplevel(root)
	root.title('Calorie Tracker')
	root.geometry('800x800')
	title = Label(wind,text='Monthly Expenditure Tracker', font=('times new roman', 35, 'bold'), fg='white', bg='black')
	title.pack()


	con = s.connect('expenditure.db') 
	c = con.cursor()


	man = StringVar(wind)
	man.set('----') 

	mandb = StringVar(wind)
	mandb.set('----')

	day = StringVar(wind)
	month = StringVar(wind)
	year = StringVar(wind)
	elec = StringVar(wind)
	intt = StringVar(wind)
	leis = StringVar(wind)
	total = StringVar(wind)

	Label1 = Label(wind, text='Day(dd)', font=('times new roman', 20)).place(relx=0.0, rely=0.1)
	Label2 = Label(wind, text='month(mm)', font=('times new roman', 20)).place(relx=0.0, rely=0.25)
	Label3 = Label(wind, text='year(yy)', font=('times new roman', 20)).place(relx=0.0, rely=0.4)
	Label4 = Label(wind, text='Electricity', font=('times new roman', 20)).place(relx=0.6, rely=0.1)
	Label5 = Label(wind, text='Internet', font=('times new roman', 20)).place(relx=0.6, rely=0.3)
	Label6 = Label(wind, text='Leisure', font=('times new roman', 20)).place(relx=0.6, rely=0.5)
	Label7 = Label(wind, text='Total', font=('times new roman', 20)).place(relx=0.0, rely=0.55)


	per = Label(wind, text='Name - ', font=('times new roman', 20)).place(relx=0.0, rely=0.175)
	cald = OptionMenu(wind, man, *person)  
	cald.place(relx=0.1,rely=0.175)


	perr = Label(wind, text='Table - ', font=('times new roman', 20)).place(relx=0.0, rely=0.9)
	caldd = OptionMenu(wind, mandb, *person) 
	caldd.place(relx=0.1,rely=0.9)


	dayT = Entry(wind, textvariable=day)
	dayT.place(relx=0.2, rely=0.1)

	monthT = Entry(wind, textvariable=month)
	monthT.place(relx=0.2, rely=0.25)

	yearT = Entry(wind, textvariable=year)
	yearT.place(relx=0.2, rely=0.4)

	elecT = Entry(wind, textvariable=elec)
	elecT.place(relx=0.8, rely=0.1)

	intT = Entry(wind, textvariable=intt)
	intT.place(relx=0.8, rely=0.3)

	leisT = Entry(wind, textvariable=leis)
	leisT.place(relx=0.8, rely=0.5)

	totalT = Entry(wind, textvariable=total)
	totalT.place(relx=0.2, rely=0.55)

	def receive():
		totals = int(elec.get())+int(intt.get())+int(leis.get()) 
		print("You have submitted a record")

		c.execute('CREATE TABLE IF NOT EXISTS ' +man.get()+ ' (Datestamp TEXT, Electricity INTEGER, Internet INTEGER, Leisure INTEGER, Total INTEGER)') #SQL syntax

		date = datetime.date(int(year.get()),int(month.get()), int(day.get())) 

		c.execute('INSERT INTO ' +man.get()+ ' (Datestamp, Electricity, Internet, Leisure, Total) VALUES (?, ?, ?, ?, ?)',
				  (date, elec.get(), intt.get(), leis.get(), totals))
		con.commit()


		man.set('----')
		mandb.set('----')
		day.set('')
		month.set('')
		year.set('')
		elec.set('')
		intt.set('')
		leis.set('')
		total.set(totals)


	def clear():
		man.set('----')
		mandb.set('----')
		month.set('')
		year.set('')
		elec.set('')
		intt.set('')
		leis.set('')
		total.set('')
	def note():
		c.execute('SELECT * FROM ' + mandb.get())

		frame = Frame(wind)
		frame.place(relx= 0.4, rely = 0.6)

		Lb = Listbox(frame, height = 8, width = 35,font=("arial", 12)) 
		Lb.pack(side = 'left')

		scroll = Scrollbar(frame, orient = 'vertical') 
		scroll.config(command = Lb.yview)
		scroll.pack(side = 'right')
		Lb.config(yscrollcommand = scroll.set) 


		Lb.insert(0, 'Date, Electricity, Internet, leisure, total')

		data = c.fetchall() 

		for row in data:
			Lb.insert(1,row) 

		L7 = Label(wind, text = mandb.get()+ '      ', 
				   font=("arial", 16)).place(relx=0.4,rely=0.55) 

		L8 = Label(wind, text = "They are ordered from most recent", 
				   font=("arial", 16)).place(relx=0.4,rely=0.85)
		con.commit()


	button_1 = Button(wind, text="Submit", command=receive)
	button_1.place(relx=0.2,rely=0.7)

	button_2 = Button(wind,text= "Clear", command=clear)
	button_2.place(relx=0.8,rely=0.7)

	button_3 = Button(wind,text="Open DB", command=note)
	button_3.place(relx=0.5,rely=0.9)	
root.mainloop()