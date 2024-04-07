from app_styleguide import *
import music_search
from tkinter import filedialog


def choose_folder():
    """Lets user choose a folder and updates the text box to say what folder"""
    folder_path = filedialog.askdirectory()

    if folder_path:
        folder_path = folder_path.replace("/", "\\")
        folder_ent.insert(tk.END, folder_path)


def output():
    """Outputting the data found in the directory chosen"""

    music_search.find_music(folder.get())


def gui():
    global folder_ent
    global folder

    folder = tk.StringVar()

    main_win.eval("tk::PlaceWindow . center")
    main_win.title("Music Search App")

    ttk.Button(main_win, text="Browse", command=choose_folder).grid(row=1, columnspan=2)

    ttk.Label(main_win, text="Folder:").grid(row=2, columnspan=2)
    folder_ent = ttk.Entry(main_win, textvariable=folder)
    folder_ent.grid(row=3, columnspan=2, ipadx=25)

    ttk.Button(main_win, text="Output", command=output).grid(row=4, columnspan=2)

    main_win.mainloop()


if __name__ == "__main__":
    gui()
