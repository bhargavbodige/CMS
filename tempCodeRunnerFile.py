
upassword.place(x=30, y=120)

password = Entry(root, show="*", font="10")
password.place(x=145, y=120)

Login = Button(text="Login", font="20", command=login)
Login.place(x=145, y=180)

RegBtn = Button(text="Register", font="20", command=register)
RegBtn.place(x=250, y=180)

root.mainloop()
