package game.logic.board;

import game.logic.player.Player;

/**
 * Contains the actual board logic.
 * I.e. methods to make a move, check validity of a move, check if the game was won
 */
public class Board {
    private int size;
    private int[][] board;

    public Board(int size) {
        this.size = size;
        this.board = new int[size][size];
    }

    public int getValue(int x, int y) {
        return board[x][y];
    }

    public Board copy() {
        Board copy = new Board(this.size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                copy.board[i][j] = this.board[i][j];
            }
        }
        return copy;
    }

    public void makeMove(Player player, int x, int y) {
        board[x][y] = player.getId();
    }

    public boolean isValidMove(int x, int y) {
        return board[x][y] == 0;
    }

    public boolean noMoveleft() {
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                if (isValidMove(x, y)) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean hasDrawn(Player player1, Player player2) {
        if (!noMoveleft()) {
            return false;
        }
        if (hasWon(player1)) {
            return false;
        } else if (hasWon(player2)) {
            return false;
        }
        return true;
    }

    public boolean hasWon(Player player) {
        for (int i = 0; i < size; i++) {
            if (checkRow(i, player.getId()) || checkCollumn(i, player.getId())) {
                return true;
            }
        }
        return checkDiagonal(player.getId());
    }

    private boolean checkDiagonal(int id) {
        boolean right = true;
        boolean left = true;
        for (int i = 0; i < size; i++) {
            if (board[i][i] != id) {
                right = false;
            }
        }
        for (int i = 0; i < size; i++) {
            if (board[size - 1 - i][i] != id) {
                left = false;
            }
        }
        return right || left;
    }

    private boolean checkRow(int row, int id) {
        for (int j = 0; j < size; j++) {
            if (board[row][j] != id) {
                return false;
            }
        }
        return true;
    }

    private boolean checkCollumn(int collumn, int id) {
        for (int j = 0; j < size; j++) {
            if (board[j][collumn] != id) {
                return false;
            }
        }
        return true;
    }

    public int getSize() {
        return size;
    }
}
