import tkinter as tk
import requests

url = "https://example.com"

def load_page(event=None):
    url = url_input.get()
    print(url)

    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        url_input.delete(0, tk.END)
        url_input.insert(0, url)

    response = requests.get(url)
    print(response.text)


window = tk.Tk()
window.geometry("800x600")
window.title("Test")

url_input = tk.Entry(window)
url_input.pack(fill="x", padx=10, pady=10)
url_input.bind("<Return>", load_page)

button = tk.Button(window, text="load", command=load_page)
button.pack()

window.mainloop()