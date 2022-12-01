package game.logic.player.ai;

import game.logic.board.Board;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RandomAiTest {

    @Test
    public void testMakeMove() {
        Board board = new Board(3);
        RandomAi player = new RandomAi(1);
        // fill the entire board and test if it's truly filled
        for (int i = 0; i < 9; i++) {
            player.makeMove(board);
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                assertEquals(board.getValue(i, j), player.getId());
            }
        }
    }
}