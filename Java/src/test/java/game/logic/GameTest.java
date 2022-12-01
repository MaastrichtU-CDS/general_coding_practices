package game.logic;

import game.logic.player.Player;
import game.logic.player.ai.AlphaBetaAi;
import game.logic.player.ai.RandomAi;
import game.logic.player.human.HumanPlayer;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class GameTest {

    @Test
    public void testGameLoop() {
        // test different sized games with random AIs
        Player player1 = new RandomAi(1);
        Player player2 = new RandomAi(2);
        for (int i = 3; i < 10; i++) {
            Game game = new Game(i, player1, player2);
            assertTrue(game.isFinished());
        }

        // test different sized games with alphabeta AIs
        player1 = new AlphaBetaAi(1);
        player2 = new AlphaBetaAi(2);
        for (int i = 3; i < 6; i++) {
            Game game = new Game(i, player1, player2);
            assertTrue(game.isFinished());
        }
    }

    @Test
    public void testAiPlayerStart() {
        // test different sized games with random AIs
        Player player1 = new AlphaBetaAi(1);
        HumanPlayer player2 = new HumanPlayer(2);
        Game game = new Game(3, player1, player2);
        game.makeMove(1, 0);
        assertEquals(game.getCellValue(0, 0), "X");
        assertEquals(game.getCellValue(1, 0), "O");
        assertEquals(game.getCellValue(0, 1), "X");
        assertEquals(game.getCurrentPlayer(), player2);

    }

}