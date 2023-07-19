package game.gui;

import game.logic.Game;

import javax.swing.*;

public class GUI {
    private JFrame frame;
    private JPanel mainPanel;
    private PlayingField field;
    private static final int SIZE = 300;

    /**
     * Main GUI frame. Creates and maintains the GUI.
     *
     * @param game
     */
    public GUI(Game game) {
        frame = new JFrame("Example game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(SIZE, SIZE);

        mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        field = new PlayingField(game);
        mainPanel.add(field);

        frame.getContentPane().add(mainPanel);
        frame.setVisible(true);
    }
}

