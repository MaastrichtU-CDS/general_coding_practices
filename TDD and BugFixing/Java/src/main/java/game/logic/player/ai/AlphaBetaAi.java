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
        return 0;
    }
}
