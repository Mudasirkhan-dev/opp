import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

class App:
    def __init__ (self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text = "Hello world"  )
        self.label.grid()

    def run(self):
        self.root.mainloop()    

App().run()
       