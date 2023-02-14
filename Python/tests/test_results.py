# -*- coding: utf-8 -*-

"""
Unit tests for game results
"""
from src.logic import TicTacToeGame
from src.logic import BOARD_SIZE
from src.logic import Move
from src.logic import Player


class TestResults:
    def test_first_diagonal(self):
        player = Player(label="X", color="blue")
        game = TicTacToeGame()
        game.process_move(Move(2, 0, player))
        game.process_move(Move(1, 1, player))
        game.process_move(Move(0, 2, player))
        assert game.has_winner() is True

    def test_second_diagonal(self):
        player = Player(label="X", color="blue")
        game = TicTacToeGame()
        game.process_move(Move(0, 0, player))
        game.process_move(Move(1, 1, player))
        game.process_move(Move(2, 2, player))
        assert game.has_winner() is True

    def test_all_rows(self):
        player = Player(label="X", color="blue")
        rows = []
        for i in range(BOARD_SIZE):
            game = TicTacToeGame()
            game.process_move(Move(i, 0, player))
            game.process_move(Move(i, 1, player))
            game.process_move(Move(i, 2, player))
            rows.append(game.has_winner())
        assert sum(rows) == 3

    def test_all_columns(self):
        player = Player(label="X", color="blue")
        cols = []
        for i in range(BOARD_SIZE):
            game = TicTacToeGame()
            game.process_move(Move(0, i, player))
            game.process_move(Move(1, i, player))
            game.process_move(Move(2, i, player))
            cols.append(game.has_winner())
        assert sum(cols) == 3

    def test_draw(self):
        game = TicTacToeGame()
        player1 = Player(label="X", color="blue")
        player2 = Player(label="O", color="green")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                condition1 = (i == 0 and j % 2 == 0)
                condition2 = (i == 1 and j % 2 == 1)
                condition3 = (i == 2 and j % 2 == 1)
                if (condition1 or condition2 or condition3):
                    game.process_move(Move(i, j, player1))
                else:
                    game.process_move(Move(i, j, player2))
        assert game.is_tied() is True
