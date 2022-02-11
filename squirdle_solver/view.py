import tkinter as tk
from tkinter.ttk import Separator
from turtle import bgcolor

from numpy import var
from squirdle_solver.models import Pokemon, PokemonGuess, TypeGuessEnum, UpDownEnum
from squirdle_solver.search_utility import SearchUtility
from squirdle_solver.utils.tkinter_utils import set_button_hover_color, update_widget_text

MAIN_BACKGROUND = "#3B4CCA"
BUTTON_BACKGROUND = "#CC0000"
BUTTON_BACKGROUND_HOVER = "#FF0000"
TEXT_BACKGROUND = "#7FCCEC"
TEXT_FOREGROUND = "#F7F6F2"
TEXT_ENTRY_FOREGROUND = "#070808"
SEPARATOR_BACKGROUND = "#FFDE00"

class UpDownCorrectRadioFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.configure(bg=MAIN_BACKGROUND)
        self.radio_var = tk.IntVar()
        self.up_radio = tk.Radiobutton(self, text="Up", value=UpDownEnum.Up.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)
        self.down_radio = tk.Radiobutton(self, text="Down", value=UpDownEnum.Down.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)
        self.correct_radio = tk.Radiobutton(self, text="Yes", value=UpDownEnum.Correct.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)

        self.up_radio.grid(row=0, column=0)
        self.down_radio.grid(row=0, column=1)
        self.correct_radio.grid(row=0, column=2)

        self.radio_var.set(0)

    def get_value(self) -> UpDownEnum:
        return UpDownEnum(self.radio_var.get())

class TypeRadioFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.configure(bg=MAIN_BACKGROUND)
        self.radio_var = tk.IntVar()
        self.incorrect_radio = tk.Radiobutton(self, text="No", value=TypeGuessEnum.Incorrect.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)
        self.out_of_radio = tk.Radiobutton(self, text="Out of Pos.", value=TypeGuessEnum.WrongPosition.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)
        self.correct_radio = tk.Radiobutton(self, text="Yes", value=TypeGuessEnum.Correct.value, variable=self.radio_var,
            bg=MAIN_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, selectcolor=TEXT_BACKGROUND, activebackground=MAIN_BACKGROUND)

        self.incorrect_radio.grid(row=0, column=0)
        self.out_of_radio.grid(row=0, column=1)
        self.correct_radio.grid(row=0, column=2)

        self.radio_var.set(0)

    def get_value(self) -> TypeGuessEnum:
        return TypeGuessEnum(self.radio_var.get())

class PokemonGuessFrame(tk.Frame):
    pokemon: Pokemon = None
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)
        self.configure(bg=MAIN_BACKGROUND)

        pokemon_name_lbl = tk.Label(self, text="Pokemon:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)
        generation_lbl = tk.Label(self, text="Generation:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)
        type_one_lbl = tk.Label(self, text="Type One:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)
        type_two_lbl = tk.Label(self, text="Type Two:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)
        height_lbl = tk.Label(self, text="Height:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)
        weight_lbl = tk.Label(self, text="Weight:", bg=MAIN_BACKGROUND, fg=TEXT_FOREGROUND)

        self.pokemon_name_entry = tk.Entry(self, width=20, bg=TEXT_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, insertbackground=TEXT_ENTRY_FOREGROUND)
        self.generation_radios = UpDownCorrectRadioFrame(self)
        self.type_one_radios = TypeRadioFrame(self)
        self.type_two_radios = TypeRadioFrame(self)
        self.height_radios = UpDownCorrectRadioFrame(self)
        self.weight_radios = UpDownCorrectRadioFrame(self)

        pokemon_name_lbl.grid(column=0, row=0)
        generation_lbl.grid(column=2, row=0)
        type_one_lbl.grid(column=4, row=0)
        type_two_lbl.grid(column=6, row=0)
        height_lbl.grid(column=8, row=0)
        weight_lbl.grid(column=10, row=0)

        self.pokemon_name_entry.grid(column=0, row=1, padx=3)
        tk.Frame(self, width=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=0, column=1, rowspan=2, sticky="ns", padx=2)
        self.generation_radios.grid(column=2, row=1)
        tk.Frame(self, width=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=0, column=3, rowspan=2, sticky="ns", padx=2)
        self.type_one_radios.grid(column=4, row=1)
        tk.Frame(self, width=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=0, column=5, rowspan=2, sticky="ns", padx=2)
        self.type_two_radios.grid(column=6, row=1)
        tk.Frame(self, width=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=0, column=7, rowspan=2, sticky="ns", padx=2)
        self.height_radios.grid(column=8, row=1)
        tk.Frame(self, width=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=0, column=9, rowspan=2, sticky="ns", padx=2)
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
            type_one=self.type_one_radios.get_value(),
            type_two=self.type_two_radios.get_value(),
            height=self.height_radios.get_value(),
            weight=self.weight_radios.get_value()
        )

class MainFrame(tk.Frame):
    pokemon_guess_frames: "list[PokemonGuessFrame]"
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        self.configure(bg=MAIN_BACKGROUND)
        self.scrollbar = tk.Scrollbar(self, bg=TEXT_BACKGROUND, troughcolor=MAIN_BACKGROUND)
        self.output_text_widget = tk.Text(self, state='disabled', yscrollcommand=self.scrollbar.set, height=10,
            bg=TEXT_BACKGROUND, fg=TEXT_ENTRY_FOREGROUND, insertbackground=TEXT_ENTRY_FOREGROUND, bd=2, wrap=tk.WORD)
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
        self.search_btn.configure(bg=BUTTON_BACKGROUND, fg=TEXT_FOREGROUND, activebackground=BUTTON_BACKGROUND_HOVER,
                       activeforeground=TEXT_FOREGROUND, bd=2, relief='groove')
        set_button_hover_color(self.search_btn, BUTTON_BACKGROUND_HOVER)

        self.output_text_widget.grid(row=0, padx=5, pady=5, sticky="ew")
        self.scrollbar.grid(row=0, column=1, sticky="ns", pady=5)

        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=1, sticky="ew", padx=2)

        pokemon_guess_1.grid(row=2, padx=5, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=3, sticky="ew", padx=2)
        pokemon_guess_2.grid(row=4, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=5, sticky="ew", padx=2)
        pokemon_guess_3.grid(row=6, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=7, sticky="ew", padx=2)
        pokemon_guess_4.grid(row=8, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=9, sticky="ew", padx=2)
        pokemon_guess_5.grid(row=10, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=11, sticky="ew", padx=2)
        pokemon_guess_6.grid(row=12, pady=2)
        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=13, sticky="ew", padx=2)
        pokemon_guess_7.grid(row=14, pady=2)

        tk.Frame(self, height=1, bd=0, bg=SEPARATOR_BACKGROUND).grid(row=15, sticky="ew", padx=2)

        self.search_btn.grid(row=16, pady=3)
        
        instructions = "Welcome to Squirdle Solver!\n" + \
            "Yes. This is cheating.\n\n" + \
            "Enter previous Pokemon guesses below.\n" + \
            "Then click Search to list possibilities.\n\n" + \
            f"Suggested first guess:\n{SearchUtility.get_suggested_guess(SearchUtility.get_full_pokemon_list())}"
        update_widget_text(self.output_text_widget, instructions)

    def search(self):
        if not self.validate_input():
            return
        pokemon_guesses = [x.get_pokemon_guess_object() for x in self.pokemon_guess_frames if x.pokemon_name_entry.get() != '']
        pokemon_list = SearchUtility.search(pokemon_guesses)

        output = ""
        if len(pokemon_list) > 0:
            suggested_guess = SearchUtility.get_suggested_guess(pokemon_list)
            output += f"Suggested Guess: {suggested_guess}\n"
            output += f"----------------------RESULTS ({str(len(pokemon_list))})----------------------\n"
            output += "\n".join([str(pokemon) for pokemon in pokemon_list])
        else:
            output = "Results: None"
        update_widget_text(self.output_text_widget, output)

    def validate_input(self):
        for pokemon_guess_frame in self.pokemon_guess_frames:
            if pokemon_guess_frame.pokemon_name_entry.get() != '' and not pokemon_guess_frame.validate_entered_pokemon():
                update_widget_text(self.output_text_widget, pokemon_guess_frame.error_text())
                return False
        return True
