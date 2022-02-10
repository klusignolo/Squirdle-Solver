import tkinter as tk
from squirdle_solver.view import MainFrame

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Squirdle Solver v1.0")
        MainFrame(self).grid()