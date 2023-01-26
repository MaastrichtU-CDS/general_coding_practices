# -*- coding: utf-8 -*-

"""
A tic-tac-toe game built with Python and Tkinter
Source: https://realpython.com/tic-tac-toe-python/
"""
from src.logic import TicTacToeGame
from src.board import TicTacToeBoard


def main():
    """Create the game's board and run its main loop"""
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == "__main__":
    main()
