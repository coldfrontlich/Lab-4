# 2 variant
import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from key_creation import key_creationing

def clicked():
    messagebox.showinfo('Ключ', key_creationing())

window = tk.Tk()
window.title("KeyGen for Hollow Knight")
window.geometry('540x320')
background = tk.PhotoImage(file = 'Hornet.png')
label1 = tk.Label( window, image = background)
label1.place(x = 0, y = 0)
button = Button(window, text='Создать ключ', command=clicked)
button.grid(column=0, row=0)
window.mainloop()

