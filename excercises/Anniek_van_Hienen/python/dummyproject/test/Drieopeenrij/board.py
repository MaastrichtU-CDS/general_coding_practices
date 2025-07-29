from players import RandomPlayer, HumanPlayer, MiniMaxPlayer


class Board:
    def __init__(self):
        self.n = self.get_board_size()
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]  # Create the board dynamically
        self.print_board()
        # empty_spots moet ook in deze class passen?
        # empty_spots = [(x, y) for x in range(self.n) for y in range(self.n) if not self.is_occupied(x, y)]

    def get_board_size(self):
        while True:
            user_input = input("Enter the board size (e.g., 3 for a 3x3 board): ")
            # Check if the input is numeric and greater than 0
            if user_input.isdigit() and int(user_input) > 0:
                return int(user_input)
            else:
                print("Invalid input. Please enter a positive integer.")

    def is_occupied(self, x, y):
        return self.matrix[x][y] != 0

    def make_move(self, input_X, input_Y, player):
        if not self.is_occupied(input_X, input_Y):
            self.matrix[input_X][input_Y] = player

    def unmake_move(self, input_X, input_Y):
        self.matrix[input_X][input_Y] = 0

    def check_draw(self):
        for row in self.matrix:
            if 0 in row:
                return False
        return True

    def check_winner(self, player):
        for row in self.matrix:
            if all(cell == player for cell in row):
                return True

        for col in range(self.n):
            if all(self.matrix[row][col] == player for row in range(self.n)):
                return True

        if all(self.matrix[i][i] == player for i in range(self.n)) or all(self.matrix[i][(self.n-1)-i] == player for i in range(self.n)):
            return True
        return False

    def print_board(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))
        print()

    def get_player_type(self, player_name):
        while True:

            player_input = input(f"Is {player_name} a human, a bot making a random move, or a bot playing minimax? Answer 'h' for human and 'r' for random, and 'm' for minimax: ").lower()
            if player_input == "h":
                return HumanPlayer(self)
            elif player_input == "r":
                return RandomPlayer(self)
            elif player_input == "m":
                return MiniMaxPlayer(self)
            else:
                print("Invalid input. Please enter 'h' for human, 'r' for random player and 'm' for minimax player")
