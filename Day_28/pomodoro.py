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
reps = 0
timer1 = None
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_clicked():
    global timer_running
    if timer1 is not None:
        window.after_cancel(timer1)
        canvas.itemconfig(timer_text, text="00:00")
        timer.config(text="Timer")
        status.config(text="")
        global reps
        reps = 0
        timer_running=False


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_button_clicked():
    global timer_running
    if not timer_running:

        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break = SHORT_BREAK_MIN * 60
        long_break = LONG_BREAK_MIN * 60
        if reps % 8 == 0:
            count_down(long_break)
            timer.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break)
            timer.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer1
    global timer_running

    if count > 0:
        timer_running = True
        count_min = math.floor(count / 60)
        count_sec = count % 60
        canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
        timer1 = window.after(1000, count_down, count - 1)

    else:
        timer_running = False
        start_button_clicked()
        mark = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += "✔"
            status.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), highlightthickness=0, bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", bg=GREEN, fg=RED, font=(FONT_NAME, 20, "bold"), command=start_button_clicked)
button1.grid(column=0, row=2)


button2 = Button(text="Reset", bg=GREEN, fg=RED, font=(FONT_NAME, 20, "bold"), command=reset_button_clicked)
button2.grid(column=2, row=2)
status = Label(font=(FONT_NAME, 20, "bold"), highlightthickness=0, bg=YELLOW, fg=GREEN)
status.grid(column=1, row=3)
window.mainloop()
