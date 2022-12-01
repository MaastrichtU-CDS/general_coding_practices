package game.logic.player.human;

import game.logic.board.Board;
import game.logic.player.Player;

/**
 * implementation of a human player
 */
public class HumanPlayer extends Player {
    public HumanPlayer(int id) {
        super(id, false);
    }

    public void makeMove(Board board, int x, int y) {
        board.makeMove(this, x, y);
    }
}
