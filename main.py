
import tkinter
from episode_renamer_ui import EpisodeRenamerUi
from missing_episodes_scanner import report_missing_episodes


class MainUi():
    def __init__(self):
        row = column = 0

        self.window = tkinter.Tk()
        self.window.title("Movie Episode Utility")
        self.window.resizable(0, 0)  # disable resizing of window
        self.window.config(padx=50, pady=50)

        self.window_title_label = tkinter.Label()
        self.window_title_label.config(
            text="Movie Episode Utility", 
            font=("Arial", 15, "bold")
            )
        self.window_title_label.config(pady=10)
        self.window_title_label.grid(row=row, column=column, columnspan=3)
        row += 1

        self.renamer_launch_btn = tkinter.Button()
        self.renamer_launch_btn.config(
            text="Episode Renamer", font=("Arial", 9, "bold"))
        self.renamer_launch_btn.config(
            command=self.launch_renamer, 
            bg="magenta")
        self.renamer_launch_btn.config(padx=20, pady=20)
        self.renamer_launch_btn.grid(row=row, column=column)
        column += 1

        self.missing_launch_btn = tkinter.Button()
        self.missing_launch_btn.config(
            text="List Missing Episodes", font=("Arial", 9, "bold"))
        self.missing_launch_btn.config(
            command=self.launch_missing_scanner,
            bg="cyan")
        self.missing_launch_btn.config(padx=20, pady=20)
        self.missing_launch_btn.grid(row=row, column=column)
        row += 1
        column = 0




        self.window.mainloop()


    def launch_renamer(self):
        self.window.destroy()
        EpisodeRenamerUi()

    
    def launch_missing_scanner(self):
        self.window.destroy()
        report_missing_episodes()
    


if __name__ == "__main__":
    MainUi()
    