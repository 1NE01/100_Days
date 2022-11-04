from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
# def reset_button_clicked():
#
#     start.config(text="Clicked me")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_clicked():
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
timer=Label(text="Timer",font=(FONT_NAME,30,"bold"),highlightthickness=0,bg=YELLOW,fg=GREEN)
timer.grid(column=1,row=0)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


button1=Button(text="Start",bg=GREEN,fg=RED,font=(FONT_NAME,20,"bold"),command=start_button_clicked)
button1.grid(column=0,row=2)

button2=Button(text="Reset",bg=GREEN,fg=RED,font=(FONT_NAME,20,"bold"))
button2.grid(column=2,row=2)
status=Label(text="✔",font=(FONT_NAME,20,"bold"),highlightthickness=0,bg=YELLOW,fg=GREEN)
status.grid(column=1,row=3)
window.mainloop()