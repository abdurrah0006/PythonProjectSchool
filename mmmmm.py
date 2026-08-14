import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd


# MySQL Connection
sms = mysql.connector.connect( host='localhost',  user='root',  password='aaaaa', database='ana')
cursor= sms.cursor()


#About Us
def word():
    n=Tk()
    n.geometry("920x400")
    n.configure(bg="DeepSkyBlue4")
    n.title("About Us")

    au="What does a student management system do? Thats a great topic! A student management system is a software application that helps educational institutions manage student-related data, such as enrollment, attendance, grades, and more. It can be really helpful for teachers, administrators, and even students themselves. A student management system for the commerce class can  handle tasks like adding, deleting, and modifying student information. It can also generate graphs to visualize student data, such as performance in each subject. This can be super helpful for teachers and administrators to track the progress of commerce students and make data-driven decisions.Student management system can manage marks for subjects like Accountancy, Informatics Practices, English, Business Studies, and Economics. Thats awesome! A student management system can definitely help with that. It allows teachers to input and update marks for each student in these subjects, making it easy to keep track of their performance over time. It can also generate reports and summaries of their marks, which can be really useful for both teachers and students. 📚📊"

    t=Label(n,height=13, font="arial 15 bold",wraplength=900,text=au,fg="midnightblue")
    t.pack()

    exit_button = Button(n, text="EXIT",width=25,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.place(x=400, y=350)
    
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

    window_width=420
    window_height=350

    screen_width=n.winfo_screenwidth()
    screen_height=n.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    n.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    
    n.title("Add Student")
    n.attributes('-alpha',0.9)
    n.configure(bg="DeepSkyBlue4")
    n.resizable(False,False)

    a=Button(n,text="Admno:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue",command=lambda:set_Text(Admno))
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
    print (query)

    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


#Deleting Student Tk
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

    s=Button(n,text="DELETE",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue",command=del_student)
    s.grid(row=11,column=2)

#Deleting Student SQL
def del_student():
    global Admno

    query = "DELETE FROM Student_Management_System WHERE Admno=" + Admno.get() + ";"
    print (query)
    
    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def mod():
    global Admno
    
    n= Tk()
    
    window_width=420
    window_height=100

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
    Admno= Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Admno.grid(row=3, column=2)

    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)

    s=Button(n,text="Modify",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue",command=modify)
    s.grid(row=11,column=2)

#Modifying Student Tk
def modify():
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

    cursor.execute("SELECT FirstName,LastName,Account,Business, Economic, IP FROM Student_Management_System WHERE Admno=" + Admno.get() + ";")
    xyz =cursor.fetchall()

    for a in xyz:
        print(a)
    

    b=Button(n,text="First_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    b.grid( row=4, column=1)
    FirstName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    FirstName.grid(row=4, column=2)
    FirstName.delete(0,END)
    FirstName.insert(0,a[0])


    c=Button(n, text="Last_Name:", width=15, height=1, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    c.grid( row=5, column=1)
    LastName = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    LastName.grid(row=5, column=2)
    LastName.delete(0,END)
    LastName.insert(0,a[1])


    f=Button(n, text="Account:", font="arial 15" , width=15, height=1,bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=6, column=1)
    Account = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Account.grid(row=6, column=2)
    Account.delete(0,END)
    Account.insert(0,a[2])


    f=Button(n, text="Business:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    f.grid(row=7, column=1)
    Business = Entry(n, font="arial 15 ", bg="DeepSkyBlue3",fg="midnightblue")
    Business.grid(row=7, column=2)
    Business.delete(0,END)
    Business.insert(0,a[3])


    g=Button(n, text="Economic:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    g.grid(row=8, column=1)
    Economic = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    Economic.grid(row=8, column=2)
    Economic.delete(0,END)
    Economic.insert(0,[4])


    h=Button(n, text="IP:", font="arial 15 ", width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue")
    h.grid(row=9, column=1)
    IP = Entry(n, font="arial 15 ",bg="DeepSkyBlue3",fg="midnightblue")
    IP.grid(row=9, column=2)
    IP.delete(0,END)
    IP.insert(0,a[5])

    
    exit_button = Button(n, text="EXIT",font='arial 10', width=15, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.grid(row=11,column=1)

    s=Button(n,text="Save",font="arial 10 ", width=15, bg="DeepSkyBlue3",fg="midnightblue", command=mod_student)
    s.grid(row=11,column=2)


#Modifying Student SQL
def mod_student():
    global Admno
    global FirstName
    global LastName
    global Account
    global Business
    global Economic
    global IP

    
    query= "UPDATE Student_Management_System SET FirstName= '" + FirstName.get() + "', LastName='" + LastName.get() + "',Account=" + Account.get() + ",Business=" + Business.get() + ",Economic=" + Economic.get() + ",IP=" + IP.get() + " where Admno=" + Admno.get() + ";"
    print (query)

    try:
        cursor.execute(query)
        sms.commit()
        messagebox.showinfo("Success", "Student modified successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

        

#Displaying All Student Tk
def all_rec():
    n = Toplevel(root)

    window_width=1340
    window_height=350

    screen_width=n.winfo_screenwidth()
    screen_height=n.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    n.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    
    n.title("All Record ")
    n.configure(bg="DeepSkyBlue4")
    
    cursor.execute("SELECT * FROM Student_Management_System;")
    Student_Management_System =cursor.fetchall()
    
    label = Label(n, text="Student Details ",font=("Calibri",40),bg="DeepSkyBlue3",fg="midnightblue")
    label.grid(row=0, columnspan=3)
    
    exit_button = Button(n, text="EXIT",font='arial 10', width=25, height=1, bg="DeepSkyBlue3",fg="midnightblue",command=n.destroy)
    exit_button.place (x=600,y=300)
    
    cols = ('Admno','FirstName', 'LastName','Account','Business', 'Economic', 'IP')
    listBox = ttk.Treeview(n, columns=cols,show='headings')
    for col in cols:
                  listBox.heading(col, tex=col)
                  listBox.grid(row=1, column=0, columnspan=2)
    for i,(Admno,FirstName,LastName,Account,Business, Economic, IP) in enumerate( Student_Management_System, start=1):
                  listBox.insert("", "end",values=(Admno,FirstName,LastName,Account,Business, Economic, IP))
    n.mainloop()


#Displaying Student graph Tk
def graphh():
    df= pd.read_sql_query("SELECT * FROM Student_Management_System;",sms)
    print(df)
    
    df.plot(kind='bar',x='Admno',y=['Account','Business','Economic','IP'], title='Status', color=['k','b','c','m'])
    plt.xlabel('Admno')
    plt.ylabel('Marks')
    plt.show()



#Main Menu
def main2():
    main2= Toplevel(root)

    window_width=400
    window_height=500

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()

    c_x=int(screen_width/2-window_width/2)
    c_y=int(screen_height/2-window_height/2)

    main2.geometry(f'{window_width}x{window_height}+{c_x}+{c_y}')
    main2.title("COMMERCE")
    main2.resizable(False,False)
    main2.attributes('-alpha',0.9)
    main2.configure(bg="DeepSkyBlue4")

    btn=Button(main2,text ="COMMERCE", width=28, height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue")
    btn.place(x=55,y=50)
    btn = Button(main2,text ="ADD RECORD  ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=add)
    btn.place(x=100,y=150)
    btn = Button(main2,text ="MODIFY RECORD  ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=mod)
    btn.place(x=100 ,y=200)
    btn = Button(main2,text="DELETE  RECORD ", width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=delete)
    btn.place(x=100,y=250)
    btn = Button(main2,text ="STATUS " ,width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=graphh)
    btn.place(x=100,y=300)
    btn = Button(main2,text ="ALL RECORD ",width=25,height=2,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=all_rec)
    btn.place(x=100,y=350)
    exit_button = Button(main2, text="EXIT",width=25,font='arial 10 bold',bg="DeepSkyBlue3",fg="midnightblue",command=main2.destroy)
    exit_button.place(x=100, y=400)

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

btn = Button(root,text ="ABOUT US ",width=28,height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue",command=word)
btn.place(x=55,y=250)

exit_button = Button(root, text="EXIT",width=28,height=3,font='arial 13 bold',bg="DeepSkyBlue3",fg="midnightblue",command=root.destroy)
exit_button.place(x=55, y=350)


root.mainloop()
