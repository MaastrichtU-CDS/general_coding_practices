
# Step 1: build the grid

n = 5

class Board:
    matrix = [[]]

    def __init__(self):
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        self.turn = "A"
        self.print_board()

    def is_occupied(self, x, y):
        return self.matrix[x][y] != 0

    def move_player_a(self, inputA_X, inputA_Y):
        self.matrix[inputA_X][inputA_Y] = "A"

    def move_player_b(self, inputB_X, inputB_Y):
        self.matrix[inputB_X][inputB_Y] = "B"

    def check_draw(self):
        for row in self.matrix:
            if 0 in row:
                return False
        return True

    def check_winner(self, player):
        for row in self.matrix:
            if all(cell == player for cell in row):
                return True

        for col in range(n):
            if all(self.matrix[row][col] == player for row in range(n)):
                return True

        if all(self.matrix[i][i] == player for i in range(n)) or all(self.matrix[i][(n-1)-i] == player for i in range(n)):
            return True
        return False
    def print_board(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))
        print()


# Create the board
board = Board()

# chatgpt
while True:
    if board.turn == "A":
        # Ask player A where they want to place their mark
        inputA_X = int(input("You are player A. Where do you want to put your mark? Give the row"))
        inputA_Y = int(input("Give the column: "))

        # Check if it is within the board
        if inputA_Y not in range(n) or inputA_X not in range(n):
            print("That move is out of range, please try again")
        # Check if there is not already an A or B
        elif board.is_occupied(inputA_X, inputA_Y):
            print("That spot is already occupied, please try again")
        else:
            board.move_player_a(inputA_X, inputA_Y)
            board.print_board()

            #  check winner
            if board.check_winner("A"):
                print("Player A wins!")
                break
            # check draw
            elif board.check_draw():
                print("It's a draw")
                break

            board.turn = "B"

    elif board.turn == "B":
        # Ask player B where they want to place their mark
        inputB_X = int(input("You are player B. Where do you want to put your mark? Give the row:"))
        inputB_Y = int(input("Give the column: "))

        # Check if it is within the board
        if inputB_Y not in range(n) or inputB_X not in range(n):
            print("That move is out of range, please try again")
        # Check if there is not already an A or B
        elif board.is_occupied(inputB_X, inputB_Y):
            print("That spot is already occupied, please try again")
        else:
            board.move_player_b(inputB_X, inputB_Y)
            board.print_board()

            #  check winner

            # check draw

            board.turn = "A"
