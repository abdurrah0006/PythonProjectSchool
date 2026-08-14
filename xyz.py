import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import *
import matplotlib.pyplot as plt

# MySQL Connection
sms = mysql.connector.connect( host='localhost',  user='root',  password='aaaaa', database='ana')
cursor= sms.cursor()


#About






#Adding Student Tk

def add():
    global Admno
    global FirstName
    global LastName
    global Account
    global Business
    global Economic
    global IP
    
    n=Tk()
    n.geometry("420x350")
    n.title("Add Student")
    n.attributes('-alpha',0.9)
    n.configure(bg="DeepSkyBlue4")
    n.resizable(False,False)
    label= Label(n,text="ADD",font="arial 15 bold")
    label.grid(row=3,column=1)

    a=Button(n,text="Admno:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    a.grid(row=3,column=1)
    Admno = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Admno.grid(row=3, column=2)

    b=Button(n,text="First_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    b.grid( row=4, column=1)
    FirstName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    FirstName.grid(row=4, column=2)

    c=Button(n, text="Last_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    c.grid( row=5, column=1)
    LastName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    LastName.grid(row=5, column=2)

    f=Button(n, text="Account:", font="arial 15" , width=15, height=1,bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=6, column=1)
    Account = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Account.grid(row=6, column=2)

    f=Button(n, text="Business:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=7, column=1)
    Business = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Business.grid(row=7, column=2)

    g=Button(n, text="Economic:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    g.grid(row=8, column=1)
    Economic = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    Economic.grid(row=8, column=2)

    h=Button(n, text="IP:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    h.grid(row=9, column=1)
    IP = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    IP.grid(row=9, column=2)
    
    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)

    s=Button(n,text="SAVE",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue",command=add_student)
    s.grid(row=11,column=2)


#Adding Student SQL
def add_student():


    
    query = "INSERT INTO Student_Management_System VALUES(" + Admno.get() + ", '" + FirstName.get() + "', '" + LastName.get() + "', " + Account.get() + ", " + Business.get() + ", " + Economic.get() + ", " + IP.get() + ");"

    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


#
def delete():
    global Admno
    
    n= Tk()
    
    window_width=420
    window_height=100

    screen_width=n.winfo_screenwidth()
    screen_height=n.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    n.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    
    n.title("Delete  Student")
    n.resizable(False,False)
    n.attributes('-alpha',0.9)
    n.configure(bg="DeepSkyBlue4")

    a=Button(n,text="Admno:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    a.grid(row=3,column=1)
    Admno= Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Admno.grid(row=3, column=2)

    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)

    s=Button(n,text="DELETE",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue", command=del_student())
    s.grid(row=11,column=2)

#
def del_student():

    

    query = f"ALTER TABLE Student_Management_System  DROP COLUMN {Admno};"

    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")




#
def modify ():
    global Admno
    global FirstName
    global LastName
    global Account
    global Business
    global Economic
    global IP

    n= Tk()

    window_width=420
    window_height=350

    screen_width=n.winfo_screenwidth()
    screen_height=n.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    n.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    
    n.title("Modify Student")
    n.resizable(False,False)
    n.attributes('-alpha',0.9)
    n.configure(bg="DeepSkyBlue4")

    a=Button(n,text="Admno:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    a.grid(row=3,column=1)
    Admno = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Admno.grid(row=3, column=2)

    b=Button(n,text="First_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    b.grid( row=4, column=1)
    FirstName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    FirstName.grid(row=4, column=2)

    c=Button(n, text="Last_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    c.grid( row=5, column=1)
    LastName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    LastName.grid(row=5, column=2)

    f=Button(n, text="Account:", font="arial 15" , width=15, height=1,bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=6, column=1)
    Account = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Account.grid(row=6, column=2)

    f=Button(n, text="Business:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=7, column=1)
    Business = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Business.grid(row=7, column=2)

    g=Button(n, text="Economic:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    g.grid(row=8, column=1)
    Economic = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    Economic.grid(row=8, column=2)

    h=Button(n, text="IP:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    h.grid(row=9, column=1)
    IP = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    IP.grid(row=9, column=2)
    
    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)

    s=Button(n,text="MODIFY",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue", command=mod_student())
    s.grid(row=11,column=2)

#
def mod_student():
    global Admno
    global FirstName
    global LastName
    global Account
    global Business
    global Economic
    global IP

    
    query = "UPDATE Student_Management_System SET FirstName= '  FirstName  ' , LastName= ' LastName ' ,Account=  Account  ,Business=  Business  ,Economic=  Economic  ,IP=  IP  where Admno=  Admno  ; "

    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student modified successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

#
def all_rec():

    # Create a Tkinter window for displaying the table
    n = Tk()
    n.geometry('1000x1000')
    n.title("Student Table")
    
    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)
    
    query ="SELECT * FROM Student_Management_System;"
    
    cursor.execute(query)
    sms.commit()
    
    data  = cursor.fetchall()
    label=Label(xyz,text="Students")
    label.grid(row=1,column=2)
    

    # Create a Treeview widget to display the data
    table = ttk.Treeview(n, columns=("Admno", "FirstName", "LastName", "Account", "Business", "Economic", "IP"), show="headings")


    table.heading("Admno", text="Admno")
    table.heading("FirstName", text="FName")
    table.heading("LastName", text="LName")
    table.heading("Account", text="Acc")
    table.heading("Business", text="Bus")
    table.heading("Economic", text="Eco")
    table.heading("IP", text="IP")

        
    # Insert the data into the Treeview
    for row in data:
        table.insert("", "end", values=query )












#Main Menu
def main2():
    main2= Toplevel(root)

    window_width=400
    window_height=535

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    main2.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    main2.title("STUDENT MANAGEMENT SYSTEM")
    main2.resizable(False,False)
    main2.attributes('-alpha',0.9)
    main2.configure(bg="DeepSkyBlue4")

    btn=Button(main2,text ="COMMERCE", width=28, height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue")
    btn.place(x=55,y=50)
    btn = Button(main2,text ="ADD RECORD  ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=add)
    btn.place(x=100,y=150)
    btn = Button(main2,text ="MODIFY RECORD  ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=modify)
    btn.place(x=100 ,y=200)
    btn = Button(main2,text="DELETE  RECORD ", width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=delete)
    btn.place(x=100,y=250)
    btn = Button(main2,text ="STATUS " ,width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue")
    btn.place(x=100,y=300)
    btn = Button(main2,text ="COMPARISON" ,width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue")
    btn.place(x=100,y=350)
    btn = Button(main2,text ="ALL RECORD ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=all_rec)
    btn.place(x=100,y=400)
    exit_button = Button(main2, text="EXIT",width=25,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=main2.destroy)
    exit_button.place(x=100, y=450)

#Starting Window 
root= Tk()

window_width=400
window_height=450

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=int(screen_width/2-window_width/2)
y=int(screen_height/2-window_height/2)

root.geometry(f'{window_width}x{window_height}+{x}+{y}')
root.title("STUDENT MANAGEMENT SYSTEM")
root.resizable(False,False)
root.attributes('-alpha',0.9)
root.configure(bg="DeepSkyBlue4")

btn=Button(root,text ="STUDENT MANAGEMENT SYSTEM ", width=28, height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue")
btn.place(x=55,y=50)

btn=Button(root,text ="GRADE 12 ", width=28, height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue",command= main2)
btn.place(x=55,y=150)

btn = Button(root,text ="ABOUT US ",width=28,height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue")
btn.place(x=55,y=250)

exit_button = Button(root, text="EXIT",width=28,height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue",command=root.destroy)
exit_button.place(x=55, y=350)


root.mainloop()
