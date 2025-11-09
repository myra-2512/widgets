from tkinter import *

root=Tk()
root.title("Getting Started With Widgets")
root.geometry("400x300")

lbl1=Label(text="Full name",fg="White",bg="darkblue")
lbl2=Label(text="Email ID",fg="White",bg="darkblue")
lbl3=Label(text="Password",fg="White",bg="darkblue")

name_entry=Entry()
email_entry=Entry()
password_entry=Entry(show="*")

def display():
    name=name_entry.get()
    greet="Hey, " + name + "\n"
    message="\nCongratulations for your new account!"

    text_box.insert(END,greet)
    text_box.insert(END,message)

text_box=Text(bg="lightgreen",fg="black")

btn=Button(text="Create account",command=display)

lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
password_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
           
