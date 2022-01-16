
import tkinter
import os
import episode_renamer


class EpisodeRenamerUi():
    def __init__(self):
        row = column = 0

        self.window = tkinter.Tk()
        self.window.title("Episode Renamer")
        self.window.resizable(0, 0)  # disable resizing of window
        self.window.config(padx=50, pady=50)

        self.window_title_label = tkinter.Label()
        self.window_title_label.config(
            text="Episode Renamer", 
            font=("Arial", 15, "bold")
            )
        self.window_title_label.config(pady=10)
        self.window_title_label.grid(row=row, column=column, columnspan=3)
        row += 1

        self.episode_title_label = tkinter.Label()
        self.episode_title_label.config(
            text="Desired Title",
            font=("Arial", 9, "bold")
        )        
        self.episode_title_label.grid(row=row, column=column, columnspan=3)
        row += 1

        self.episode_title_input = tkinter.Entry()
        self.episode_title_input.config(width=40)
        self.episode_title_input.grid(row=row, column=column, columnspan=2)
        row += 1

        # create a gap in the grid using empty element
        tkinter.Label().grid(row=row, column=column)
        row += 1

        self.rename_btn = tkinter.Button()
        self.rename_btn.config(
            text="Rename Episodes", font=("Arial", 9, "bold"))
        self.rename_btn.config(command=self.rename_episodes, bg="magenta")
        self.rename_btn.config(padx=20, pady=20)
        self.rename_btn.grid(row=row, column=column)
        column += 1

        self.unrename_btn = tkinter.Button()
        self.unrename_btn.config(
            text="Undo Renaming", font=("Arial", 9, "bold"))
        self.unrename_btn.config(command=self.unrename_episodes, bg="cyan")
        self.unrename_btn.config(padx=20, pady=20)
        self.unrename_btn.grid(row=row, column=column)
        row += 1
        column = 0

        self.path_label = tkinter.Label()
        working_dir = os.getcwd()
        path_info = f"Path: {working_dir}"
        if len(working_dir) > 50:
            path_info = f"Path: ...{working_dir[-50:]}"
        self.path_label.config(text=path_info, font=("Arial", 8, "bold"))
        self.path_label.config(pady=10)
        self.path_label.grid(row=row, column=column, columnspan=3)

    
        # keep UI active
        self.window.mainloop()


    def rename_episodes(self):
        desired_title = self.episode_title_input.get().strip()
        self.window.destroy()        
        if desired_title:
            episode_renamer.rename_episodes(desired_title=desired_title)


    def unrename_episodes(self):
        self.window.destroy()
        episode_renamer.unrename_episodes()        


if __name__ == "__main__":
    EpisodeRenamerUi()
    