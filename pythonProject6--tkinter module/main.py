from tkinter import *
from tkinter import messagebox

def OK():
    user_name= e1.get()
    password= e2.get()
    if user_name==""and password=="":
        messagebox.showinfo("","Blanked places are not accepted")
    elif password=="1234"and user_name=="Admin":
        messagebox.showinfo("","Login succesfully")
        root.destroy()
    else:
        messagebox.showinfo("","incorect user_name and password entered")
root=Tk()
root.title("Login--page")
root.geometry("300x400")
global e1
global e2
Label(root,text="user_name").place(x=10,y=10)
Label(root,text="password").place(x=10,y=40)
e1=Entry(root)
e1.place(x=90,y=10)
e2=Entry(root)
e2.place(x=90,y=45)
e2.config(show="*")
Button(root,text="Login",command=OK,bg="blue",width=7).place(x=90,y=75)

root.mainloop()
