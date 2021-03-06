import tkinter
import os

UNSELECTED_COLOR = "grey"
SELECTED_COLOR = "green"

PROGRAM_DIR = os.path.dirname(
                            os.path.dirname(os.path.realpath(__file__)))

class EpisodeParseUi:
    output_positions = None

    def __init__(self, episode:str, pattern_count:int, total_patterns:int, gui_output:list):
        global output_positions
        output_positions = gui_output

        row = column = 0

        # main UI
        self.window = tkinter.Tk()
        self.window.title("Episode Parser")
        self.window.resizable(0, 0)  # disable resizing of window
        self.window.config(padx=30, pady=30)


        info_label = tkinter.Label()
        info_label.config(
            text="Select ONLY the buttons corresponding to the episodes", 
            font=("Arial", 12, "bold"))
        info_label.grid(row=row, column=column, columnspan=len(episode))
        row += 1

        # Add example image
        # 248 x 26 (image dimensions)
        example_img_raw = tkinter.PhotoImage(file=f"{PROGRAM_DIR}/example.png")
        canvas = tkinter.Canvas(width=248, height=26)
        example_image = canvas.create_image(124, 13, image=example_img_raw)
        canvas.grid(row=row, column=column, columnspan=len(episode))
        row += 1

        # create a gap in the grid using empty element
        tkinter.Label().grid(row=row, column=column)
        row += 1

        pattern_count_label = tkinter.Label()
        pattern_count_label.config(
            text=f"Naming pattern {pattern_count} of {total_patterns} patterns", 
            font=("Arial", 9, "bold"))
        pattern_count_label.grid(
            row=row, 
            column=column, 
            columnspan=len(episode))
        row += 1

        self.number_buttons = []

        extension_index = episode.rindex(".")
        for index, character in enumerate(episode):
            if character.isdigit() and index < extension_index:
                number_button = tkinter.Button()
                self.number_buttons.append(number_button)


                number_button.config(
                    text=character, font=("Arial", 9, "bold"), 
                    bg=UNSELECTED_COLOR, fg="cyan")
                number_button.grid(row=row, column=column)
            else:
                character_label = tkinter.Label()
                character_label.config(
                    text=character, font=("Arial", 9, "bold"), 
                    fg="magenta")
                character_label.grid(row=row, column=column)
            column += 1
        row += 1
        column = 0

        # empty element to fill the grid
        tkinter.Label().grid(row=row, column=column)
        row += 1

        confirm_button = tkinter.Button()
        confirm_button.config(
            text="Confirm", font=("Arial", 9, "bold"), 
            bg=UNSELECTED_COLOR)
        confirm_button.config(command=self.register_episode_positions)
        confirm_button.grid(row=row, column=column, columnspan=len(episode))
       

        # button functions -- decorated to target each button separately
        for i, btn in enumerate(self.number_buttons):
            def action(index=i):
                def color_toggle():
                    if self.number_buttons[index]["bg"] == UNSELECTED_COLOR:
                        self.number_buttons[index].config(bg=SELECTED_COLOR)
                    else:
                        self.number_buttons[index].config(bg=UNSELECTED_COLOR)
                return color_toggle

            self.number_buttons[i].config(command=action(i))


        # keep UI active
        self.window.mainloop()


    def register_episode_positions(self):
        global output_positions

        positions = []
        for index, btn in enumerate(self.number_buttons):
            if btn['bg'] == SELECTED_COLOR:
                positions.append(index)

        output_positions.extend(positions)

        # close the ui
        self.window.destroy()
