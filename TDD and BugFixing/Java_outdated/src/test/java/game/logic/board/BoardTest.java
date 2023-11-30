package game.logic.board;

import game.logic.player.Player;
import game.logic.player.ai.RandomAi;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class BoardTest {
    private static final int SIZE = 3;

    @Test
    public void testHasWon() {
        Board board = new Board(SIZE);
        Player player = new RandomAi(1);
        //test the diagonal from top right to bottom left
        board.makeMove(player, 2, 0);
        board.makeMove(player, 1, 1);
        board.makeMove(player, 0, 2);
        assertTrue(board.hasWon(player));

        //test rows
        board = new Board(SIZE);
        board.makeMove(player, 0, 0);
        board.makeMove(player, 0, 1);
        board.makeMove(player, 0, 2);
        assertTrue(board.hasWon(player));
    }
}