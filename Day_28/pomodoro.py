from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25* 60
SHORT_BREAK_SEC = 5* 60
LONG_BREAK_SEC =25 * 60
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
    global reps
    if not timer_running:






        if reps ==7:
            status.config(text="✔✔✔✔")
            reps = -1
            time2=LONG_BREAK_SEC
            timer.config(text="Long Break", fg=RED)
        elif not reps % 2 == 0:
            time2=SHORT_BREAK_SEC
            timer.config(text="Short Break", fg=PINK)
        else:
            time2=WORK_SEC
            timer.config(text="Work", fg=GREEN)
        reps += 1
        count_down(time2)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer1
    global timer_running
    global reps

    if count > 0:
        timer_running = True
        count_min = math.floor(count / 60)
        count_sec = count % 60
        canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
        timer1 = window.after(1000, count_down, count - 1)

    else:
        timer_running = False

        if not reps == 7:
            status.config(text="{0:✔^{1}}".format("", int(reps/ 2)))
        start_button_clicked()


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
