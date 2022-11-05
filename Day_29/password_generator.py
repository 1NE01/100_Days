# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.config(padx=20,pady=20,bg="white")
canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.pack()










window.mainloop()