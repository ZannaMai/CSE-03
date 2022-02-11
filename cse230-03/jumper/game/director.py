import random
from game.words import Word
from game.play import Play
from game.parachute import Parachute

class Director:

    def __init__(self):
        self._words = Word
        self._play = Play
        self._parachute = Parachute

    def start_game(self, get_word):
        self._words(get_word)
        self._play(self._word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            self._word = self._get_word()
            self._play(self._word)
        return get_word

    def parachute(self, show_parachute):
        self._parachute(show_parachute)