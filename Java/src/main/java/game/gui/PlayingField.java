package game.gui;

import game.logic.Game;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Creates and maintains the actual playing field
 * Communicates with the game logic whenever a move is made by a player clicking on a button
 */
public class PlayingField extends JPanel {
    private int size;
    private Game game;
    private JButton[][] field;

    public PlayingField(Game game) {
        this.size = game.getSize();
        this.game = game;
        this.setLayout(new GridLayout(size, size));
        field = new JButton[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                JButton button = new JButton();
                field[i][j] = button;
                button.setText(game.getCellValue(i, j));
                button.addActionListener(createButtonListener());
                this.add(button);
            }
        }
    }

    /**
     * Method used to reset what is shown on a button after a move is made
     */
    public void revalidateButtonText() {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                field[i][j].setText(game.getCellValue(i, j));
            }
        }
        this.repaint();
    }

    /**
     * Creates a listener that triggers the game logic after a button is pressed
     *
     * @return
     */
    private ActionListener createButtonListener() {
        return new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JButton button = (JButton) e.getSource();
                for (int i = 0; i < size; i++) {
                    for (int j = 0; j < size; j++) {
                        if (field[i][j] == e.getSource()) {
                            if (game.isValidMove(i, j)) {
                                String status = game.makeMove(i, j);
                                if (status != null) {
                                    JOptionPane.showMessageDialog(null, status + "Game over");
                                }
                            }
                        }
                    }
                }
                PlayingField f = (PlayingField) button.getParent();
                f.revalidateButtonText();
            }
        };
    }
}
