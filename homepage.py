import ViewComplaints
from tkinter import *
import Login
global c1

def fun(root, U_ID):
    import tkinter as tk
    import mysql.connector as c
    connection = c.connect(host="localhost", user="root", passwd="admin", database="complaintmanagementsystem")
    cursor = connection.cursor()
    cursor.execute("select * from users")
    phone = ""
    for row in cursor.fetchall():
        if row[3] == U_ID:
            phone = row[0]
    
    phonenumber = U_ID
    places = []
    cmplnttype = []
    cursor.execute("select * from address")
    for row in cursor.fetchall():
        places.append(row[1])
    cursor.execute("select * from c_types")
    for row in cursor.fetchall():
        cmplnttype.append(row[1])
    root2 = tk.Tk()
    root2.title("Register Complaint")
    root2.geometry("600x600")
    root2.resizable(False,False)
    root2.config(bg="orange")
    
    # Place
    l1 = tk.Label(root2, text="Place", font=("Century Gothic bold",12))
    l1.place(x=50,y=50)

    # dropdown for places
    def show_places():
        label.config(text=dd1.get())
    dd1 = StringVar()
    dd1.set("Andheri")
    drop = OptionMenu(root2, dd1, *places)
    drop.config(font=("Century Gothic bold",12), width=15)
    drop.place(x=250,y=50)

    # shows complaints for that particular user
    def viewcomplains(U_ID2=phone):
        # root2.destroy()
        ViewComplaints.fun1(root2, U_ID2)

    # view complaint button
    bt1 = tk.Button(root2, text="View Complaints",
                    width=15, command=viewcomplains)
    bt1.place(x=480,y=1)

    # Complaint Types
    l2 = tk.Label(root2, text="Complaint Type",font=("Century Gothic bold",12))
    l2.place(x=50,y=120)

    def show_duties():
        label.config(text=dd2.get())

    dd2 = StringVar()
    dd2.set("WaterIssue")
    drop = OptionMenu(root2, dd2, *cmplnttype)
    drop.config(font=("Century Gothic bold",12),width=15)
    drop.place(x=250,y=120)
    # drop.grid(row=2, column=1)

    def registr(U_ID2 = U_ID):
        import tkinter as tk
        import mysql.connector as c
        
        connection = c.connect(host="localhost", user="root", passwd="admin", database="complaintmanagementsystem")
        cursor = connection.cursor()
        
        ctid = ""
        cursor.execute("select * from c_types")
        
        for row in cursor.fetchall():
            if row[1] == dd2.get(): 
                ctid = row[0]
                break
        
        a_id = ""
        cursor.execute("select * from address")
        
        for row in cursor.fetchall():
            if row[1] == dd1.get():
                a_id = row[0]
                break
        cursor.execute("select * from users")
        
        phone = ""
        for row in cursor.fetchall():
            if row[3] == U_ID2:
                phone = row[0]
        phonenumber = U_ID
        print(txtArea.get("1.0", END))
        cursor.execute("select * from complaints")
        
        cid = ""
        for row in cursor.fetchall():
            cid = row[0]
        U_id2 = cid[0:2]
        n = int(cid[-1])+1
        cid = U_id2+str(n)
        qry = "insert into complaints values(%s,%s,%s,%s,%s,%s)"
        val = (cid, txtArea.get("1.0", END), "False", a_id, ctid, phone)
        cursor.execute(qry, val)
        connection.commit()
        txtArea.delete("1.0", END)
        #txtArea.insert(END,a_id)
        #txtArea.insert(END,phone)

    # Complaint Description
    l3 = tk.Label(root2, text="Complaint Description",font=("Century Gothic bold",12))
    l3.place(x=50,y=200)
    txtArea = Text(root2, height=7, width=35)
    txtArea.place(x=250,y=200)

    # Register Button
    btn = tk.Button(root2, text="Register Complaint", font=("Century Gothic bold",12), width=20, command=registr)
    btn.place(x=85,y=400)
    
    # Define a function to clear the input text
    def clearToTextInput():
        txtArea.delete("1.0","end")

    # Clear Button
    clr = tk.Button(root2, text="Clear", font=("Century Gothic bold",12), width=20, command=clearToTextInput)
    clr.place(x=300,y=400)
    
    root2.mainloop()
