from tkinter import *
import _praw_rip
import _R2T_bot

# command function for the button


def process_request():
    sub = subredt_entry.get()
    num = int(num_entry.get())
    msg = msg_entry.get()

    manual_set = _praw_rip.PullCategory(f"{sub}", num)
    _R2T_bot.send_cute_bot(manual_set, f"{msg}")

    return "Task Completed!"


# made the window
the_window = Tk()
the_window.title("R2T Control")

# declared the instructions
instructions_sub = Label(the_window, text="Please enter a Subreddit:\n")
instructions_num = Label(the_window, text="\nEnter how many to send:\n")
instructions_msg = Label(the_window, text="\nWhat would you like to say?:\n")

# make the entries
subredt_entry = Entry(the_window)
num_entry = Entry(the_window)
msg_entry = Entry(the_window)

# make the finish button
button_push = Button(the_window, text="Press When Ready",
                     command=process_request)

# packing it in order
instructions_sub.pack()
subredt_entry.pack()
instructions_num.pack()
num_entry.pack()
instructions_msg.pack()
msg_entry.pack()
button_push.pack()

the_window.mainloop()
