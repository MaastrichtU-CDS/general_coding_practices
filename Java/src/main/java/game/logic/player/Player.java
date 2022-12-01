package game.logic.player;

import game.logic.board.Board;

/**
 * Abstract player class, allows us to create different human and AI variants that use the same core-logic
 * so we can plug them in when needed
 */
public abstract class Player {
    private int id;
    private Player opponent;
    private boolean ai;

    public Player(int id, boolean ai) {
        this.id = id;
        this.ai = ai;
    }

    public int getId() {
        return id;
    }

    public void makeMove(Board board) {
    }

    public boolean isAi() {
        return ai;
    }

    public void setOpponent(Player opponent) {
        this.opponent = opponent;
    }

    public Player getOpponent() {
        return this.opponent;
    }
}
