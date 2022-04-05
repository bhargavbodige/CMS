from tkinter import *
import tkinter as tk
import mysql.connector as c
connection = c.connect(host="localhost", user="root", passwd="admin", database="complaintmanagementsystem")
cursor = connection.cursor()

def reg():
    def submit_value():
        U_id = "U_1"
        gender = ""
        if var.get() == 1:
            gender = "Male"
        elif var.get() == 2:
            gender = "Female"
        
        print("id=", U_id)
        print("name=", name.get())
        print("sge=", age.get())
        print("pghonnumber=", phonenumber.get())
        print(gender)
        print("email=", email.get())
        print("password=", password.get())
        cursor.execute("select*from users")
        for row in cursor.fetchall():
            U_id = row[0]
        U_id2 = U_id[0:2]      
        n = int(U_id[-1])+1   
        U_id = U_id2+str(n)
        
        qry = "insert into users values(%s,%s,%s,%s,%s,%s,%s)"
        val = (U_id, name.get(), age.get(), phonenumber.get(),
            gender, email.get(), password.get())
        cursor.execute(qry, val)
        connection.commit()
        
        name.delete(0, END)
        phonenumber.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
        age.delete(0, END)
        confpassword.delete(0, END)
    
    root8 = tk.Tk()
    Label(root8, text="Registration Form", font="times 15 bold",
        bg="red", fg="white").pack(fill="both")
    l1 = Label(root8, text="Enter Name", font="14")
    l1.place(x=30, y=70)
    name = Entry(root8, font="10")
    name.place(x=200, y=70)
    
    l2 = Label(root8, text="Enter Age", font="14")
    l2.place(x=30, y=120)
    age = Entry(root8, font="10")
    age.place(x=200, y=120)
    
    l3 = Label(root8, text="Phone Number", font="14")
    l3.place(x=30, y=170)
    phonenumber = Entry(root8, font="10")
    phonenumber.place(x=200, y=170)
    
    l4 = Label(root8, text="Select Gender", font="14")
    l4.place(x=30, y=220)
    var = IntVar()
    c = Checkbutton(root8, text="Male", variable=var, onvalue=1)
    c.place(x=200, y=220)
    var1 = IntVar()
    c1 = Checkbutton(root8, text="Female", variable=var, onvalue=2)
    c1.place(x=250, y=220)
    
    l5 = Label(root8, text="Enter Email", font="14")
    l5.place(x=30, y=270)
    email = Entry(root8, font="10")
    email.place(x=200, y=270)
    
    l6 = Label(root8, text="Enter Password", font="14")
    l6.place(x=30, y=320)
    password = Entry(root8, show="*", font="10")
    password.place(x=200, y=320)
    
    l7 = Label(root8, text="Confirm Password", font="14")
    l7.place(x=30, y=370)
    confpassword = Entry(root8, show="*", font="10")
    confpassword.place(x=200, y=370)
    
    Button(text="Register", font="20", command=submit_value).place(x=200, y=450)
    
    root8.title("Registration")
    root8.geometry("600x600")
    root8.resizable(False, False)
    root8.mainloop()
