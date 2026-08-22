from tkinter import *
from tkinter import ttk
import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)


# print("Time's up!")

# def start_timer(*args):
#     try:
#         value = float(timevalue.get())
#     except ValueError:
#         pass
current_time = ""
def start_timer(*args):
    try:
        pomodoro = int(float(timevalue.get())) 
        for x in range(pomodoro, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            current_time = {seconds}
            print(current_time)
            time.sleep(1)
    except ValueError:
        pass


root = Tk()
root.title("Timer")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

timevalue = StringVar()
timevalue_entry = ttk.Entry(mainframe, width=7, textvariable=timevalue)
timevalue_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Start", command=start_timer).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter time: ").grid(column=1, row=1, sticky=W)

ttk.Label(mainframe, text=current_time).grid(column=1, row=2, sticky=S)

root.columnconfigure(0, weight=10)
root.rowconfigure(0, weight=10)
mainframe.columnconfigure(2, weight=10)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
timevalue_entry.focus()
root.bind("<Return>", start_timer)

root.mainloop()






