from numpy import mean
from squirdle_solver.models import Pokemon, PokemonGuess, UpDownEnum
from squirdle_solver.utils.file_utils import file_path
import statistics
import math
import json

class SearchUtility:
    @staticmethod
    def search(pokemon_guesses: "list[PokemonGuess]") -> "list[Pokemon]":
        """Returns a list of matching Pokemon"""
        filtered_pokemon = SearchUtility.get_full_pokemon_list()
        for pokemon_guess in pokemon_guesses:
            filtered_pokemon = SearchUtility.filter_pokemon_list_by_guess(
                list_to_filter=filtered_pokemon,
                pokemon_guess=pokemon_guess
            )
        return filtered_pokemon
    
    @staticmethod
    def get_full_pokemon_list() -> "list[Pokemon]":
        filepath = file_path('pokemon.json')
        file = open(filepath)
        pokemon_list = json.loads(file.read())
        file.close()
        return [Pokemon(**pokemon_dict) for pokemon_dict in pokemon_list]

    @staticmethod
    def get_pokemon(pokemon_name: str) -> Pokemon:
        matching_pokemon = [pokemon for pokemon in SearchUtility.get_full_pokemon_list() if pokemon.name.lower() == pokemon_name.lower()]
        if len(matching_pokemon) == 1:
            return matching_pokemon[0]
        else:
            return None

    @staticmethod
    def filter_pokemon_list_by_guess(list_to_filter: "list[Pokemon]", pokemon_guess: PokemonGuess) -> "list[Pokemon]":
        filtered_list = list_to_filter.copy()
        if pokemon_guess.generation == UpDownEnum.Up:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.generation > pokemon_guess.pokemon.generation]
        elif pokemon_guess.generation == UpDownEnum.Down:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.generation < pokemon_guess.pokemon.generation]
        else:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.generation == pokemon_guess.pokemon.generation]

        if pokemon_guess.type_one:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.type_one == pokemon_guess.pokemon.type_one]
        else:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.type_one != pokemon_guess.pokemon.type_one]

        if pokemon_guess.type_two:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.type_two == pokemon_guess.pokemon.type_two]
        else:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.type_two != pokemon_guess.pokemon.type_two]

        if pokemon_guess.weight == UpDownEnum.Up:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.weight > pokemon_guess.pokemon.weight]
        elif pokemon_guess.weight == UpDownEnum.Down:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.weight < pokemon_guess.pokemon.weight]
        else:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.weight == pokemon_guess.pokemon.weight]

        if pokemon_guess.height == UpDownEnum.Up:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.height > pokemon_guess.pokemon.height]
        elif pokemon_guess.height == UpDownEnum.Down:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.height < pokemon_guess.pokemon.height]
        else:
            filtered_list = [pokemon for pokemon in filtered_list if pokemon.height == pokemon_guess.pokemon.height]

        return filtered_list
    
    @staticmethod
    def get_suggested_guess(filtered_pokemon_list: "list[Pokemon]") -> Pokemon:
        median_generation = math.floor(statistics.median([pokemon.generation for pokemon in filtered_pokemon_list]))
        mean_weight = math.floor(statistics.mean([pokemon.weight for pokemon in filtered_pokemon_list]))
        mean_height = math.floor(statistics.mean([pokemon.height for pokemon in filtered_pokemon_list]))
        target_generation_pokemon = [pokemon for pokemon in filtered_pokemon_list if pokemon.generation == median_generation]
        minimum_deviation = 1000000
        best_match: Pokemon = None
        for pokemon in target_generation_pokemon:
            weight_deviation = abs(pokemon.weight - mean_weight)
            height_deviation = abs(pokemon.height - mean_height)
            deviation_sum = weight_deviation + height_deviation
            if deviation_sum < minimum_deviation:
                best_match = pokemon
        return best_match
