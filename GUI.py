from tkinter import *
import tkinter.messagebox
 
window = Tk()
window.title("Audio Converter")
window.geometry('550x500')

class Application :
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=800,height=740,bg='skyblue')
        self.left.pack(side=LEFT)


btn = Button(window, text="Audio 1")
btn.grid(column=1, row=0)
self.left=Frame(master,width=800,height=740,bg='skyblue')
self.left.pack(side=LEFT)

btn = Button(window, text="Audio 2")
btn.grid(column=1, row=0)
self.left=Frame(master,width=800,height=740,bg='skyblue')
self.left.pack(side=LEFT)

btn = Button(window, text="Audio 3")
btn.grid(column=1, row=0)
self.left=Frame(master,width=800,height=740,bg='skyblue')
self.left.pack(side=LEFT)

btn = Button(window, text="Audio 4")
btn.grid(column=1, row=0)
window.mainloop()
