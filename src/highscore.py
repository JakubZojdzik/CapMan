import os
from data import Data

class Highscore:
    highscores = []

    @staticmethod
    def set_highscore(score, lvl, difficulty, save=True):
        Highscore.highscores[lvl][difficulty] = score
        if save:
            Highscore.save_highscores()

    @staticmethod
    def create_highscores_file():
        content = '0\t0\t0'
        for _ in range(7):
            content += '\n-1\t-1\t-1'
        Data.create_file('highscores.txt', content)

    @staticmethod
    def load_highscores():
        Highscore.highscores = [[int(score) for score in lvl.split('\t')] for lvl in Data.read_from_file('highscores.txt').split('\n')]

    @staticmethod
    def save_highscores():
        content = '\n'.join('\t'.join(str(score) for score in lvl) for lvl in Highscore.highscores)
        Data.write_to_file('highscores.txt', content)

    @staticmethod
    def is_locked(lvl, difficulty):
        return Highscore.highscores[lvl][difficulty] == -1

    @staticmethod
    def lock(lvl, difficulty):
        Highscore.set_highscore(-1, lvl, difficulty)

    @staticmethod
    def unlock(lvl, difficulty):
        if Highscore.is_locked(lvl, difficulty):
            Highscore.set_highscore(0, lvl, difficulty)

Highscore.create_highscores_file()
Highscore.load_highscores()