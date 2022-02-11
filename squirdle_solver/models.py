from dataclasses import dataclass
from enum import Enum

@dataclass
class Pokemon:
    name: str
    generation: int
    type_one: str
    type_two: str
    height: int
    weight: int

    def __str__(self) -> str:
        type_str = self.type_one if self.type_two == 'none' else f"{self.type_one}/{self.type_two}"
        return f"{self.name} | Gen {self.generation} | {type_str} | H: {self.height} | W: {self.weight}"

class UpDownEnum(Enum):
    Up = 0
    Down = 1
    Correct = 2

class TypeGuessEnum(Enum):
    Incorrect = 0
    Correct = 1
    WrongPosition = 2

@dataclass
class PokemonGuess:
    pokemon: Pokemon
    generation: UpDownEnum
    type_one: TypeGuessEnum
    type_two: TypeGuessEnum
    height: UpDownEnum
    weight: UpDownEnum