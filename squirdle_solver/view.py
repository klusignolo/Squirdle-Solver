import tkinter as tk
from tkinter.ttk import Separator

from numpy import var
from squirdle_solver.models import Pokemon, PokemonGuess, UpDownEnum
from squirdle_solver.search_utility import SearchUtility
from squirdle_solver.utils.tkinter_utils import update_widget_text

class UpDownCorrectRadioFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.radio_var = tk.IntVar()
        self.up_radio = tk.Radiobutton(self, text="Up", value=UpDownEnum.Up.value, variable=self.radio_var)
        self.down_radio = tk.Radiobutton(self, text="Down", value=UpDownEnum.Down.value, variable=self.radio_var)
        self.correct_radio = tk.Radiobutton(self, text="Yes", value=UpDownEnum.Correct.value, variable=self.radio_var)

        self.up_radio.grid(row=0, column=0)
        self.down_radio.grid(row=0, column=1)
        self.correct_radio.grid(row=0, column=2)

        self.radio_var.set(0)

    def get_value(self) -> UpDownEnum:
        return UpDownEnum(self.radio_var.get())

class PokemonGuessFrame(tk.Frame):
    pokemon: Pokemon = None
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.type_one_check_var = tk.BooleanVar(False)
        self.type_two_check_var = tk.BooleanVar(False)

        pokemon_name_lbl = tk.Label(self, text="Pokemon:")
        generation_lbl = tk.Label(self, text="Generation:")
        type_one_lbl = tk.Label(self, text="Type One:")
        type_two_lbl = tk.Label(self, text="Type Two:")
        height_lbl = tk.Label(self, text="Height:")
        weight_lbl = tk.Label(self, text="Weight:")

        self.pokemon_name_entry = tk.Entry(self, width=20)
        self.generation_radios = UpDownCorrectRadioFrame(self)
        self.type_one_check = tk.Checkbutton(self, variable=self.type_one_check_var)
        self.type_two_check = tk.Checkbutton(self, variable=self.type_two_check_var)
        self.height_radios = UpDownCorrectRadioFrame(self)
        self.weight_radios = UpDownCorrectRadioFrame(self)

        pokemon_name_lbl.grid(column=0, row=0)
        generation_lbl.grid(column=2, row=0)
        type_one_lbl.grid(column=4, row=0)
        type_two_lbl.grid(column=6, row=0)
        height_lbl.grid(column=8, row=0)
        weight_lbl.grid(column=10, row=0)

        self.pokemon_name_entry.grid(column=0, row=1)
        Separator(self, orient=tk.VERTICAL).grid(row=0, column=1, rowspan=2, sticky="ns", padx=2)
        self.generation_radios.grid(column=2, row=1)
        Separator(self, orient=tk.VERTICAL).grid(row=0, column=3, rowspan=2, sticky="ns", padx=2)
        self.type_one_check.grid(column=4, row=1)
        Separator(self, orient=tk.VERTICAL).grid(row=0, column=5, rowspan=2, sticky="ns", padx=2)
        self.type_two_check.grid(column=6, row=1)
        Separator(self, orient=tk.VERTICAL).grid(row=0, column=7, rowspan=2, sticky="ns", padx=2)
        self.height_radios.grid(column=8, row=1)
        Separator(self, orient=tk.VERTICAL).grid(row=0, column=9, rowspan=2, sticky="ns", padx=2)
        self.weight_radios.grid(column=10, row=1)

    def error_text(self) -> str:
        pokemon_name = self.pokemon_name_entry.get()
        return f"Pokemon {pokemon_name} not found"

    def validate_entered_pokemon(self) -> bool:
        pokemon_name = self.pokemon_name_entry.get()
        self.pokemon = SearchUtility.get_pokemon(pokemon_name)
        return not self.pokemon is None

    def get_pokemon_guess_object(self) -> PokemonGuess:
        return PokemonGuess(
            pokemon=self.pokemon,
            generation=self.generation_radios.get_value(),
            type_one=self.type_one_check_var.get(),
            type_two=self.type_two_check_var.get(),
            height=self.height_radios.get_value(),
            weight=self.weight_radios.get_value()
        )

class MainFrame(tk.Frame):
    pokemon_guess_frames: list[PokemonGuessFrame]
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        self.scrollbar = tk.Scrollbar(self)
        self.output_text_widget = tk.Text(self, state='disabled', yscrollcommand=self.scrollbar.set, height=10)
        self.scrollbar.config(command=self.output_text_widget.yview)

        pokemon_guess_1 = PokemonGuessFrame(self)
        pokemon_guess_2 = PokemonGuessFrame(self)
        pokemon_guess_3 = PokemonGuessFrame(self)
        pokemon_guess_4 = PokemonGuessFrame(self)
        pokemon_guess_5 = PokemonGuessFrame(self)
        pokemon_guess_6 = PokemonGuessFrame(self)
        pokemon_guess_7 = PokemonGuessFrame(self)
        self.pokemon_guess_frames = [
            pokemon_guess_1,
            pokemon_guess_2,
            pokemon_guess_3,
            pokemon_guess_4,
            pokemon_guess_5,
            pokemon_guess_6,
            pokemon_guess_7
        ]

        self.search_btn = tk.Button(self, width=35, text="Search", command=self.search)

        self.output_text_widget.grid(row=0, padx=5, pady=5, sticky="ew")
        self.scrollbar.grid(row=0, column=1, sticky="ns", pady=5)

        Separator(self, orient="horizontal").grid(row=1, sticky="ew", padx=2)

        pokemon_guess_1.grid(row=2, padx=5, pady=2)
        Separator(self, orient="horizontal").grid(row=3, sticky="ew", padx=2)
        pokemon_guess_2.grid(row=4, pady=2)
        Separator(self, orient="horizontal").grid(row=5, sticky="ew", padx=2)
        pokemon_guess_3.grid(row=6, pady=2)
        Separator(self, orient="horizontal").grid(row=7, sticky="ew", padx=2)
        pokemon_guess_4.grid(row=8, pady=2)
        Separator(self, orient="horizontal").grid(row=9, sticky="ew", padx=2)
        pokemon_guess_5.grid(row=10, pady=2)
        Separator(self, orient="horizontal").grid(row=11, sticky="ew", padx=2)
        pokemon_guess_6.grid(row=12, pady=2)
        Separator(self, orient="horizontal").grid(row=13, sticky="ew", padx=2)
        pokemon_guess_7.grid(row=14, pady=2)

        Separator(self, orient="horizontal").grid(row=15, sticky="ew", padx=2)

        self.search_btn.grid(row=16, pady=3)
        
        instructions = "Welcome to Squirdle Solver!\n" + \
            "Yes. This is cheating.\n\n" + \
            "Enter previous Pokemon guesses below.\n" + \
            "Then click Search to list possibilities."
        update_widget_text(self.output_text_widget, instructions)

    def search(self):
        if not self.validate_input():
            return
        pokemon_guesses = [x.get_pokemon_guess_object() for x in self.pokemon_guess_frames if x.pokemon_name_entry.get() != '']
        pokemon_list = SearchUtility.search(pokemon_guesses)

        output = ""
        if len(pokemon_list) > 0:
            output += f"Possible Pokemon ({str(len(pokemon_list))}):\n" + "\n".join([str(pokemon) for pokemon in pokemon_list])
        else:
            output = "Results: None"
        update_widget_text(self.output_text_widget, output)

    def validate_input(self):
        for pokemon_guess_frame in self.pokemon_guess_frames:
            if pokemon_guess_frame.pokemon_name_entry.get() != '' and not pokemon_guess_frame.validate_entered_pokemon():
                update_widget_text(self.output_text_widget, pokemon_guess_frame.error_text())
                return False
        return True
