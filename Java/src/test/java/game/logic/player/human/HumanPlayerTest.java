package game.logic.player.human;

import game.logic.board.Board;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class HumanPlayerTest {

    @Test
    public void testMakeMove() {
        HumanPlayer player = new HumanPlayer(1);
        Board board = new Board(3);
        player.makeMove(board, 0, 0);
        assertEquals(board.getValue(0, 0), player.getId());
    }
}