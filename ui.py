import tkinter

class Ui:
    def __init__(self, episode:str):
        row = column = 0

        # main UI
        self.window = tkinter.Tk()
        self.window.title("Episode Renamer")
        self.window.resizable(0, 0)  # disable resizing of window
        self.window.config(padx=30, pady=30)

        info_label = tkinter.Label()
        info_label.config(text="Select ONLY the buttons containing the episodes", font=("Arial", 9, "bold"))
        info_label.grid(row=row, column=column, columnspan=len(episode))
        row += 1

        gap_label = tkinter.Label()
        gap_label.config(text=" ", font=("Arial", 9, "bold"))
        gap_label.grid(row=row, column=column, columnspan=len(episode))
        row += 1

        self.number_buttons = []

        for character in episode:
            if character.isdigit():
                number_button = tkinter.Button()
                self.number_buttons.append(number_button)

                number_button.config(text=character, font=("Arial", 9, "bold"), bg="gray", command=None)
                number_button.grid(row=row, column=column)
            else:
                character_label = tkinter.Label()
                character_label.config(text=character, font=("Arial", 9, "bold"))
                character_label.grid(row=row, column=column)
            column += 1

        # keep UI active
        self.window.mainloop()



if __name__ == "__main__":
    gui = Ui("Fairytale S05 Ep 14")