from tkinter import *
scrn=Tk()
scrn.title("Checking clicks")
scrn.minsize(width=500,height="300")
label=Label(text="🕵‍",font=("Arial",40,"bold"))
label.pack()
input= Entry(width=10)
input.pack()

def button_clicked():
    label.config(text=f"CHANGED:{input.get()}")
button=Button(text="click me",command=button_clicked)
button.pack()
mainloop()




