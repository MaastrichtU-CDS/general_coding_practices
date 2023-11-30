package game.main;

import game.gui.GUI;
import game.logic.Game;
import game.logic.player.Player;
import game.logic.player.ai.AlphaBetaAi;
import game.logic.player.human.HumanPlayer;

public final class MainLoop {
    // Main loop of the proram, seperate from all other logic.
    private MainLoop() {
    }

    private static final Player PLAYER1 = new HumanPlayer(1);
    private static final Player PLAYER2 = new AlphaBetaAi(2);
    private static final int SIZE = 3;

    public static void main(String[] args) {
        new GUI(new Game(SIZE, PLAYER1, PLAYER2));
    }
}
