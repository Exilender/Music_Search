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
    "Version.TLabel",
    font=("arial", 7),
    anchor="center",
    width=25,
    foreground="#410917",
    background="#F0C3C5",
)
style.configure("Divider.TLabel", background="#F0C3C5")

style.configure(
    "TButton",
    font=("arial", 10),
    width=15,
    relief="flat",
    foreground="white",
    background="#E8888E",
)
style.configure(
    "Wider.TButton",
    font=("arial", 10),
    width=20,
    relief="flat",
    foreground="white",
    background="#E8888E",
)

style.configure("TMenubutton", foreground="white", background="#E41E4F")
