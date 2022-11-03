from tkinter import *
scrn=Tk()
scrn.title("Miles to KM")
scrn.minsize(width=100,height=100)
scrn.config(padx=20,pady=20)
# input= Entry(width=10)

input = Scale(from_=0, to=100, orient="horizontal")

input.grid(column=2+1,row=1+1)
label=Label(text="Miles",font=("Arial",10,"bold"))
label.grid(column=3+1,row=1+1)
label2=Label(text="is equal to:",font=("Arial",10,"bold"))
label2.grid(column=0+1+1,row=1+1+1)
label3=Label(text="0",font=("Arial",10,"bold"))
label3.grid(column=1+1+1,row=1+1+1)

def button_clicked():
    a=int(input.get()) * 1.609
    label3.config(text=f"{a}")
button=Button(text="click me",command=button_clicked)
label4=Label(text="Km",font=("Arial",10,"bold"))
label4.grid(column=2+1+1,row=1+1+1)
button.grid(column=1+1+1,row=2+1+1)


mainloop()