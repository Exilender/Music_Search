""" Style guide for Music Search App """

import tkinter as tk
import tkinter.ttk as ttk

main_win = tk.Tk()

main_win.configure(background="#F0C3C5")
ttk.Style().theme_use("default")
style = ttk.Style()

style.configure(
    "TLabel",
    font=("arial", 10, "bold"),
    anchor="center",
    width=25,
    foreground="#410917",
    background="#FFEBEB",
)

style.configure(
    "Divider.TLabel",
    background="#F0C3C5",
)

style.configure(
    "TButton",
    font=("arial", 10),
    width=15,
    relief="flat",
    foreground="white",
    background="#E8888E",
)
