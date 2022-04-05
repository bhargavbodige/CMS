from tkinter import *

def fun1(root, U_ID):
    import tkinter as tk
    from tkinter import ttk
    import homepage
    
    root3 = tk.Tk()
    
    import mysql.connector as c
    connection = c.connect(host="localhost", user="root",
                           passwd="admin", database="complaintmanagementsystem")
    cursor = connection.cursor()
    
    my_tree = ttk.Treeview(root3)
    my_tree['columns'] = ("Complain Id", "Complain",
                          "ComplainType", "complainstatus", "Address")
    my_tree.column("Complain Id", width=50, minwidth=50, anchor=tk.CENTER)
    my_tree.column("Complain", width=100, minwidth=150, anchor=tk.CENTER)
    my_tree.column("ComplainType", width=50, minwidth=150, anchor=tk.CENTER)
    my_tree.column("complainstatus", width=150, minwidth=150, anchor=tk.CENTER)
    my_tree.column("Address", width=150, minwidth=100, anchor=tk.CENTER)
    my_tree.heading("Complain Id", text="Complaint Id", anchor=tk.CENTER)
    my_tree.heading("Complain", text="Complaint", anchor=tk.CENTER)
    my_tree.heading("ComplainType", text="Complaint Type", anchor=tk.CENTER)
    my_tree.heading("complainstatus",
                    text="Complaint Solved", anchor=tk.CENTER)
    my_tree.heading("Address", text="Address", anchor=tk.CENTER)
    cursor.execute("select*from complaints")
    i = 1
    for row in cursor.fetchall():
        if row[5] == U_ID:
            address = ""
            cursor2 = connection.cursor()
            cursor2.execute("select * from address")
            for row2 in cursor.fetchall():
                if row2[0] == row[3]:
                    address = row2[1]
            cursor3 = connection.cursor()
            ct = ""
            cursor3.execute("select * from c_types")
            for row3 in cursor3.fetchall():
                if row3[0] == row[4]:
                    ct = row3[1]
            my_tree.insert('', i, text="", values=(
                row[0], row[1], ct, row[2], address))
            i += 1        
    my_tree.pack()
    
    root3.title("View complains")
    root3.geometry("800x400")
    root3.resizable(False,False)
    root3.config(bg="green")
    root3.mainloop()
