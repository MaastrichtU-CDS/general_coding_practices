package game.logic.player.ai;

import game.logic.board.Board;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AlphaBetaAiTest {

    @Test
    public void testMakeMoveArbitraryBoardSize() {
        for (int size = 3; size < 6; size++) {
            Board board = new Board(size);
            AlphaBetaAi player1 = new AlphaBetaAi(1);
            AlphaBetaAi player2 = new AlphaBetaAi(2);
            player1.setOpponent(player2);
            player2.setOpponent(player1);

            // fill the entire board and test if it's truly filled
            for (int i = 0; i < size * size; i++) {
                player1.makeMove(board);
            }
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    assertEquals(board.getValue(i, j), player1.getId());
                }
            }
        }
    }
}