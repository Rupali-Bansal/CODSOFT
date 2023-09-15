
import tkinter as tk
from tkinter import *
import tkinter.messagebox

window = tk.Tk()
window.title("to do list")


def Add_task():
    content = task_entry.get()
    todo_box.insert(END, content)
    task_entry.delete(0,tk.END)

def update():
    selected_task_index = todo_box.curselection()[0]
    update_task = task_entry.get()

    if update_task:
        todo_box.delete(selected_task_index)
        todo_box.insert(selected_task_index,update_task)
        task_entry.delete(0,tk.END)

 
            
label = tk.Label(window, text = "To-Do-List-App", font = 'arial 25 bold', width = 10, bd = 5, bg = 'orange', fg = 'black')
label.pack(side = 'top',fill = BOTH)
list_frame = tk.Frame(window)
list_frame.pack()

todo_box = tk.Listbox(list_frame, bd = 5, height=20, width=50)
todo_box.pack(side=tk.LEFT)

scroller = tk.Scrollbar(list_frame)
scroller.pack(side = tk.RIGHT, fill = tk.Y)

todo_box.config(yscrollcommand=scroller.set)
# scroller.config(command=list_frame.yview)

task_entry = tk.Entry(window, bd = 5, text='Enter..........', width=40, font = 'arial, 10 bold')
task_entry.pack()

add_task_btn = tk.Button(window,bd = 5, text = "Add Task", command = Add_task,  width = 30,font = ("arial,25,bold"), background='yellow')
add_task_btn.pack()

update_task_btn = tk.Button(window, bd = 5,  text = "Update Task", command = update, width = 30,font = ("arial,25,bold"), background='green')
update_task_btn.pack()

window.mainloop()   