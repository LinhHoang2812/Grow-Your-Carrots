from tkinter import *
import pygame

GREEN = "#A2B38B"
BEIGE = "#FFFBE7"
PINK = "#CC704B"
RED = "#e7305b"
SKIN = "#DAB88B"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_NAME = "Courier"
reps = 0
carrot_marks = ""
timer = None

# Sound effect
pygame.mixer.init()


def play_sound():
    pygame.mixer.music.load("Cool-sms-tone.mp3")
    pygame.mixer.music.play()


# Timer reset


def timer_reset():
    global reps, timer
    window.after_cancel(timer)
    titel_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    warning()
    reps = 0




def warning():
    if reps > 1:
        warning_text.config(text="Your dog has eaten\n all your carrots 🐩")


# Timer start


def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    warning_text.config(text="")


    if reps % 8 == 0:
        timer_count(long_break_sec)
        titel_label.config(text="Long Break 🥳", fg=SKIN)
    elif reps % 2 == 0:
        timer_count(short_break_sec)
        titel_label.config(text="Short Break ☕️", fg=SKIN)
    else:
        timer_count(work_sec)
        titel_label.config(text="Work Time 💻", fg=PINK)


# Timer count
def timer_count(count):
    global carrot_marks,timer

    count_min = int(count // 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, timer_count, count - 1)

    else:
        play_sound()
        if reps % 2 != 0:
            carrot_marks += "🥕"
        carrots.config(text=carrot_marks)
        timer_start()


# UI set up

window = Tk()
window.title("Grow your carrots")
window.config(padx=100, pady=50, bg=BEIGE)
window.geometry("530x450")


carrot_image = PhotoImage(file="carrot-2.png")
canvas = Canvas(width=170, height=250, bg=BEIGE, highlightthickness=0)
canvas.create_image(85, 130, image=carrot_image)
timer_text = canvas.create_text(85, 150, text="00:00", fill="white", font=(FONT_NAME, 50))
canvas.grid(column=1, row=1)

titel_label = Label(text="Timer", font=(FONT_NAME, 30), bg=BEIGE, fg=GREEN)
titel_label.grid(column=1, row=0)

carrots = Label(font=(FONT_NAME, 20), bg=BEIGE)
carrots.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=lambda:[warning(),timer_reset()])
reset_button.grid(column=2, row=2)

warning_text = Label(font= (FONT_NAME,20),bg=BEIGE, fg=RED)
warning_text.grid(column=1, row=4)

window.mainloop()
