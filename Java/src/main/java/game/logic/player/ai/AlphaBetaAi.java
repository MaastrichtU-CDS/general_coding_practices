package game.logic.player.ai;

import game.logic.board.Board;
import game.logic.player.Player;

/**
 * Implementation of an AI that uses the AlphaBeta algorithm to make a move
 */
public class AlphaBetaAi extends Player {
    //Max depth is the number of moves the AI can look ahead
    //The higher the number the more accurate its predictions and the slower the AI becomes
    private final int maxDepth = 5;
    //min/max value used for the ALPHABETA calculations, all values will be in the range between [-ALPHABETA,ALPHABETA]
    private static final int ALPHABETA = 3;

    public AlphaBetaAi(int id) {
        super(id, true);
    }

    public void makeMove(Board board) {

        int bestX = -1;
        int bestY = -1;
        int value = -ALPHABETA;
        int size = board.getSize();
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                if (!board.isValidMove(x, y)) {
                    continue;
                }
                Board copy = board.copy();
                copy.makeMove(this, x, y);
                int temp = alphabeta(copy, maxDepth - 1, -ALPHABETA, ALPHABETA, false);

                if (temp > value) {
                    value = temp;
                    bestX = x;
                    bestY = y;
                }
            }
        }
        board.makeMove(this, bestX, bestY);
    }


    private int alphabeta(Board board, int depth, int alpha, int beta, boolean max) {
        if (board.hasWon(this)) {
            //player has won so value is high
            return 1;
        } else if (board.hasWon(super.getOpponent())) {
            //player has lost so value is low
            return -1;
        } else if (board.hasDrawn(this, super.getOpponent())) {
            //player has reached a draw so value is neutral
            return 0;
        } else if (depth > 0) {
            //Neither player has won, nor is there a draw and we're not yet at the maximum depth so check childeren
            // moves
            if (max) {
                // looking at maximizing players moves
                int size = board.getSize();
                int value = -ALPHABETA - +1;
                for (int x = 0; x < size; x++) {
                    for (int y = 0; y < size; y++) {
                        if (!board.isValidMove(x, y)) {
                            continue;
                        }
                        Board copy = board.copy();
                        copy.makeMove(this, x, y);
                        int temp = alphabeta(copy, depth - 1, alpha, beta, false);
                        if (temp > value) {
                            value = temp;
                            if (value >= beta) {
                                break;
                            }
                        }
                        if (value > alpha) {
                            alpha = value;
                        }
                    }
                }
                return value;
            } else {
                // looking at opponent moves, so minimizing player
                int size = board.getSize();
                int value = 2;
                for (int x = 0; x < size; x++) {
                    for (int y = 0; y < size; y++) {
                        if (!board.isValidMove(x, y)) {
                            continue;
                        }
                        Board copy = board.copy();
                        copy.makeMove(super.getOpponent(), x, y);
                        int temp = alphabeta(copy, depth - 1, alpha, beta, true);
                        if (temp < value) {
                            value = temp;
                            if (value <= alpha) {
                                break;
                            }
                        }
                        if (value < beta) {
                            beta = value;
                        }
                    }
                }
                return value;
            }
        } else {
            //reached maximum depth, noone has won and no draw, so return neutral value
            return 0;
        }
    }
}
