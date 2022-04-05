from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
def ad():
    def viewresult():
        import mysql.connector as c
        connection=c.connect(host="localhost",user="root",passwd="admin",database="complaintmanagementsystem")
        cursor=connection.cursor()
        cursor.execute("select*from complaints")
        solved=0
        unsolved=0
        for row in cursor.fetchall():
            if row[2]=="False":
                solved+=1
            elif row[2]=="True":
                unsolved+=1
        print(solved)
        print(unsolved)
        x=["Solved","Unsolved"]
        h=[]
        h.append(unsolved)
        h.append(solved)
        c=["green","red"]
        plt.bar(x,h,width=0.4,color=c)
        plt.xlabel("Complaints")
        plt.ylabel("Scale")
        plt.show()
    root5=tk.Tk()
    Result=Button(text="View Result",font="20",command=viewresult)
    Result.pack()
    root5.title("Admin")
    root5.geometry("600x600")
    root5.mainloop()
