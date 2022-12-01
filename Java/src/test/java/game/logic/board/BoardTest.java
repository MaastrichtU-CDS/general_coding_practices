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

        board = new Board(SIZE);
        //test the diagonal from top left to bottom right
        board.makeMove(player, 0, 0);
        board.makeMove(player, 1, 1);
        board.makeMove(player, 2, 2);
        assertTrue(board.hasWon(player));

        //test all rows
        for (int i = 0; i < SIZE; i++) {
            board = new Board(SIZE);
            board.makeMove(player, i, 0);
            board.makeMove(player, i, 1);
            board.makeMove(player, i, 2);
            assertTrue(board.hasWon(player));
        }
        //test all collumns
        for (int i = 0; i < SIZE; i++) {
            board = new Board(SIZE);
            board.makeMove(player, 0, i);
            board.makeMove(player, 1, i);
            board.makeMove(player, 2, i);
            assertTrue(board.hasWon(player));
        }
    }

    @Test
    public void testDraw() {
        Board board = new Board(SIZE);
        Player player1 = new RandomAi(1);
        Player player2 = new RandomAi(2);
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if ((i == 0 && j % 2 == 0) || (i == 1 && j % 2 == 1) || (i == 2 && j % 2 == 1)) {
                    board.makeMove(player1, i, j);
                } else {
                    board.makeMove(player2, i, j);
                }
            }
        }

        assertTrue(board.hasDrawn(player1, player2));
    }

}