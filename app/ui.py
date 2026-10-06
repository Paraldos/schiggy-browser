import tkinter as tk
from app.browser import load_page

def start_ui():
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Test")

    url_input = tk.Entry(window)
    url_input.pack(fill="x", padx=10, pady=10)
    url_input.bind("<Return>", lambda event: load_page(url_input.get()))

    button = tk.Button(
        window,
        text="load",
        command=lambda: load_page(url_input.get())
    )
import tkinter as tk
from app.browser import load_page

def start_ui():
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Test")

    url_input = tk.Entry(window)
    url_input.pack(fill="x", padx=10, pady=10)
    url_input.bind("<Return>", lambda event: load_page(url_input.get()))

    button = tk.Button(
        window,
        text="load",
        command=lambda: load_page(url_input.get())
    )
    button.pack()

    window.mainloop()