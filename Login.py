from tkinter import *
import tkinter as tk
import mysql.connector as c
import homepage
import Registration
import admin

connection = c.connect(host="localhost", user="root", passwd="admin", database="complaintmanagementsystem")
cursor = connection.cursor()

def login():
    if uid.get()=="0000" and password.get()=="0000":
        root.destroy()
        admin.ad()
    cursor.execute("select U_phonenuber,password from users")
    flag = 0
    uid2 = ""
    for row in cursor.fetchall():
        if row[0] == uid.get() and row[1] == password.get():
            flag = 1
            uid2 = row[0]
            root.destroy()
            homepage.fun(root, uid2)
    
    if flag == 0:
        print("Login failed")

def register():
    root.destroy()
    Registration.reg()


root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)

Label(root, text="L O G I N", font="times 15 bold",bg="red", fg="white").pack(fill="both")
root.title("Login")

enterid = Label(root, text="Phone No", font="20")
enterid.place(x=30, y=70)

uid = Entry(root, font="10")
uid.place(x=145, y=70)

upassword = Label(root, text="Password", font="20")
upassword.place(x=30, y=120)

password = Entry(root, show="*", font="10")
password.place(x=145, y=120)

Login = Button(text="Login", font="20", command=login)
Login.place(x=145, y=180)

RegBtn = Button(text="Register", font="20", command=register)
RegBtn.place(x=250, y=180)

root.mainloop()
