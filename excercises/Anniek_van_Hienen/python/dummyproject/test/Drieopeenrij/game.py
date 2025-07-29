from board import Board  # Board class from board.py

#Setup: defining board size and players
board = Board()  # Initialize the board

# Create player A and player B based on user input
player_A = board.get_player_type("player A")
player_B = board.get_player_type("player B")

# Game loop
current_player = player_A  # Player A starts
player_mark = "A"  # Mark for player A
other_player = "B"
while True:
    current_player.make_move(player_mark, other_player)

    # Check if the current player has won
    if board.check_winner(player_mark):
        print(f"Player {player_mark} wins!")
        break

    # Check if it's a draw
    if board.check_draw():
        print("It's a draw!")
        break

    # Switch players
    if current_player == player_A:
        current_player = player_B
        player_mark = "B"
        other_player = "A"
    else:
        current_player = player_A
        player_mark = "A"
        other_player = "B"
