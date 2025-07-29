# Define the Player class
import random
import copy
import time


class Player:
    def __init__(self, board):
        self.board = board

    def is_occupied(self, x, y):
        return self.board.matrix[x][y] != 0


# Define the HumanPlayer class
class HumanPlayer(Player):
    def make_move(self, player, other_player):
        while True:
            try:
                input_X = int(input(f"You are player {player}. Where do you want to put your mark? Give the row: "))
                input_Y = int(input("Give the column: "))

                # Check if it is within the board
                if input_X not in range(self.board.n) or input_Y not in range(self.board.n):
                    print("That move is out of range, please try again.")
                    continue

                # Check if the spot is occupied
                if self.is_occupied(input_X, input_Y):
                    print("That spot is already occupied, please try again.")
                    continue

                self.board.make_move(input_X, input_Y, player)
                self.board.print_board()
                break
            except ValueError:
                print("Invalid input, please enter a number.")


# Define the RandomPlayer class
class RandomPlayer(Player):
    def make_move(self, player, other_player):
        empty_spots = [(x, y) for x in range(self.board.n) for y in range(self.board.n) if not self.is_occupied(x, y)]

        if empty_spots:
            input_X, input_Y = random.choice(empty_spots)
            self.board.make_move(input_X, input_Y, player)
            self.board.print_board()

class MiniMaxPlayer(Player):
    def make_move(self, player, other_player):
        start = time.time()
        move = self.minimax(self.board, 5, player, player, other_player)
        print(time.time()-start)
        self.board.make_move(move[0], move[1], player)
        self.board.print_board()


    def evaluate(self, board, MAX, MIN):

        matrix = board.matrix
        n = board.n

        if board.check_winner(MIN):  # deze weet niet of het om zichzelf of een andere gaat
            return -10000
        elif board.check_winner(MAX):
            return 10000
        elif board.check_draw():
            return 0
        else:
            score = 0

            lines = self.get_all_lines(matrix, n)

            for line in lines:
                max_count = line.count(MAX)
                min_count = line.count(MIN)

                # dit kan verder uitgebouwd worden naar andere "slimme zetten"behalve dingen blocken
                # gegarandeerde rijen bij 3x3 en 4x4, "onblokkeerbare rijen"
                # Only consider unblocked lines (either MAX or MIN, not both)
                if max_count > 0 and min_count == 0:
                    score += 10 ** max_count
                elif min_count > 0 and max_count == 0:
                    score -= 10 ** min_count

            return score

    def get_all_lines(self, matrix, n):
        lines = []

        # All rows
        for row in matrix:
            lines.append(row)

        # All columns
        for col in range(n):
            line = [matrix[row][col] for row in range(n)]
            lines.append(line)

        # Main diagonal (top-left to bottom-right)
        lines.append([matrix[i][i] for i in range(n)])

        # Anti diagonal (top-right to bottom-left)
        lines.append([matrix[i][n - 1 - i] for i in range(n)])

        return lines

    def minimax(self, board, depth, current_player, MAX, MIN):
        empty_spots = [(x, y) for x in range(board.n) for y in range(board.n) if not board.is_occupied(x, y)]

        # iets om te definieren welke speler max't
        if current_player == MAX:
            best_score = [-1, -1, -99999]
        else:
            best_score = [-1, -1, 99999]

        if current_player == "A":
            other_player = "B"
        else:
            other_player = "A"

        if (depth == 0 or board.check_winner(other_player) == True or board.check_draw() == True):
            score = self.evaluate(board, MAX, MIN)
            return [-1, -1, score]

        for spot in empty_spots:
            x = spot[0]
            y = spot[1]
            board.make_move(x, y, current_player)
            score = self.minimax(board, depth - 1, other_player, MAX, MIN)
            board.unmake_move(x, y)
            score[0] = x
            score[1] = y


            if current_player == MAX:
                if score[2] > best_score[2]:
                    best_score = score
            else:
                if score[2] < best_score[2]:
                    best_score = score
        return best_score






