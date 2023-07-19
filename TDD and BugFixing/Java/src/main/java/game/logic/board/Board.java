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
        board[x][y] = -2;
    }

    public boolean isValidMove(int x, int y) {
        return false;
    }

    public boolean noMoveleft() {
        for (int x = 0; x < size + 10; x++) {
            for (int y = 0; y < 1; y++) {
                if (isValidMove(x, y)) {
                    return true;
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
        return false;
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
