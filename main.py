import math
from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
task = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global task
    task = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global task
    task = 1
    count_down(WORK_MIN*60)

def left_zero(number):
    return f"00{number}"[-2:]

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    global task

    if task % 8 == 0:
        timer_text.config(text="Break",fg=RED)
    else:
        if task % 2 == 0:
            timer_text.config(text="Break",fg=PINK)
        else:
            timer_text.config(text="Work",fg=GREEN)

    counter_min = left_zero(math.floor(counter/60))
    counter_sec = left_zero(counter%60)

    canvas.itemconfig(canvas_text,text=f"{counter_min}:{counter_sec}")
    if counter >= 0 and task > 0:
        window.after(1000,count_down,counter-1)
        if counter < 10:
            winsound.Beep(1000, 440)
    else:
        if task != 0:
            task += 1
            check_mark.config(text="✓" * math.floor(task / 2))

            if task % 8 == 0:
                counter = LONG_BREAK_MIN*60
            else:
                if task % 2 == 0:
                    counter = SHORT_BREAK_MIN*60
                else:
                    counter = WORK_MIN*60
            window.after(1000,count_down,counter)
        else:
            canvas.itemconfig(canvas_text, text=f"00:00")
            timer_text.config(text="Timer", fg=GREEN)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)

timer_text = Label(text = "Timer",font=(FONT_NAME,35,"normal"),bg=YELLOW,fg=GREEN)
timer_text.grid(column=2,row=1)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

start_button = Button(text="Start",font=(FONT_NAME,8,"bold"),bg=YELLOW,command=start_timer)
start_button.grid(column=1,row=3)

reset_button = Button(text="Reset",font=(FONT_NAME,8,"bold"),bg=YELLOW,command=reset_timer)
reset_button.grid(column=3,row=3)

check_mark = Label(text="",font=(FONT_NAME,12,"bold"),bg=YELLOW,fg=GREEN)
check_mark.grid(column=2,row=4)

window.mainloop()