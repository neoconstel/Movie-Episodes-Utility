import tkinter

class Ui:
    def __init__(self):

        # main UI
        self.window = tkinter.Tk()
        self.window.title("Episode Renamer")
        self.window.resizable(0, 0)  # disable resizing of window
        # self.window.config(padx=30, pady=30)


        # keep UI active
        self.window.mainloop()