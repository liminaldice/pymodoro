import tkinter as tk
import time

root = tk.Tk()


root.geometry("500x500")
root.title("GUI")

label = tk.Label(root, text="Hello, World!", font=('Liberation Mono', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Liberation Mono', 16))
textbox.pack(padx=10)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text="1")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(button_frame, text="2")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(button_frame, text="3")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

button_frame.pack(fill='x')

another_button = tk.Button(root, text="Another")
another_button.place(x=200, y=200, height=100, width=100)

root.mainloop()


