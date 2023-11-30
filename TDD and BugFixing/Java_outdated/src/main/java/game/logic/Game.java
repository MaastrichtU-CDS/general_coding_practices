package game.logic;

import game.logic.board.Board;
import game.logic.player.Player;
import game.logic.player.human.HumanPlayer;

/**
 * Main class fo the game logic
 * Keeps track of whos turn it is and if one of the players has won etc.
 */
public class Game {
    private Board board;
    private Player player1;
    private Player player2;
    private int size;

    private Player currentPlayer;

    public Game(int size, Player player1, Player player2) {
        this.size = size;
        board = new Board(size);
        this.player1 = player1;
        this.player2 = player2;

        this.player1.setOpponent(player2);
        this.player2.setOpponent(player1);

        currentPlayer = player1;

        if (player1.isAi()) {
            // if the current player is an AI player immeadiatly make a move
            makeMove(0, 0);
        }
    }

    public boolean isFinished() {
        return checkGameStatus() != null;
    }

    public boolean isValidMove(int x, int y) {
        return board.isValidMove(x, y);
    }

    public String makeMove(int x, int y) {
        String status = null;
        if (!currentPlayer.isAi()) {
            if (isValidMove(x, y)) {
                ((HumanPlayer) currentPlayer).makeMove(board, x, y);
                status = checkGameStatus();
                if (status != null) {
                    return status;
                }
                switchPlayer();
            }
        }
        if (currentPlayer.isAi()) {
            currentPlayer.makeMove(board);
            status = checkGameStatus();
            if (status != null) {
                return status;
            }
            switchPlayer();
            if (currentPlayer.isAi()) {
                //if the new player is also an AI player, keep making moves
                return makeMove(0, 0);
            }
        }
        return status;
    }

    private String checkGameStatus() {
        if (board.hasWon(currentPlayer)) {
            return "Player " + currentPlayer.getId() + " has won";
        } else if (board.hasDrawn(player1, player2)) {
            return "It's a draw!";
        } else {
            return null;
        }
    }

    private void switchPlayer() {
        if (currentPlayer == player1) {
            currentPlayer = player2;
        } else {
            currentPlayer = player1;
        }
    }

    public Player getCurrentPlayer() {
        return currentPlayer;
    }

    public String getCellValue(int x, int y) {
        if (board.getValue(x, y) == player1.getId()) {
            return "X";
        } else if (board.getValue(x, y) == player2.getId()) {
            return "O";
        } else {
            return "";
        }
    }

    public int getSize() {
        return size;
    }

}
