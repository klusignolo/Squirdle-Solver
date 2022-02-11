import tkinter as tk
from tkinter.ttk import Widget

def update_widget_text(widget: tk.Widget, value):
    """Takes updates the widget's text to equal whatever Value is specified."""
    if isinstance(widget, tk.Entry):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete(0, tk.END)
            widget.insert(0, value)
            widget.config(state="disabled")
        else:
            widget.delete(0, tk.END)
            widget.insert(0, value)
    elif isinstance(widget, tk.Text):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
            widget.config(state="disabled")
        else:
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
    elif isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
        widget.config(text=value)



def set_button_hover_color(button: tk.Widget, hover_color: str):
    """Sets the background to the hover color when mouse is over btn. Doesn't work for disabled buttons."""
    original_background = button['bg']
        
    def on_enter(button: tk.Widget):
        """Sets the background to the hover color when mouse is over btn. Doesn't work for disabled buttons."""
        if button['state'] == 'normal':
            button['bg'] = hover_color

    def on_leave(button: tk.Widget):
        """Sets the background back to default background when mouse leaves."""
        button['bg'] = original_background
    
    button.bind("<Enter>", lambda _: on_enter(button))
    button.bind("<Leave>", lambda _: on_leave(button))