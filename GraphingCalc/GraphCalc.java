/**
 * GraphCalc.java
 *
 * Graphing calculator program (class with main method)
 *
 * @author Jonathan Kim
 * CSCI 235, Wheaton College, Spring 2023
 * Project 7
 *
 * Date? April 27, 2023
 */


import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GraphCalc {
    /**
     * The paintpanel: graphPanel
     */
    private static PaintPanel graphPanel;

    /**
     * Constructor.
     */
    public GraphCalc() {
        //the window
        JFrame window = new JFrame("Graphing Calculator");
        window.setLayout(new FlowLayout());
        window.setSize(350, 600);

        //the graph panel
        graphPanel = new PaintPanel(300, 300);
        window.add(graphPanel);

        //text field for function
        JTextField funcField = new JTextField(25);
        JLabel funcLabel = new JLabel("f(x) = ");


        //found on api documentation
        funcLabel.setLabelFor(funcField);

        //panel for function
        JPanel funcPanel = new JPanel();
        funcPanel.setLayout(new FlowLayout());
        funcPanel.add(funcLabel);
        funcPanel.add(funcField);
        window.add(funcPanel);

        //textfields for x and y min and max values
        JTextField xminField = new JTextField(5);
        JTextField yminField = new JTextField(5);
        JTextField xmaxField = new JTextField(5);
        JTextField ymaxField = new JTextField(5);


        //presetting text
        xminField.setText("-10");
        yminField.setText("-10");
        xmaxField.setText("10");
        ymaxField.setText("10");

        //panel to hold range info
        JPanel rangePanel = new JPanel();
        rangePanel.setLayout(new GridLayout(2, 4));
        rangePanel.add(new JLabel("x min:"));
        rangePanel.add(xminField);
        rangePanel.add(new JLabel("y min:"));
        rangePanel.add(yminField);
        rangePanel.add(new JLabel("x max:"));
        rangePanel.add(xmaxField);
        rangePanel.add(new JLabel("y max:"));
        rangePanel.add(ymaxField);

        window.add(rangePanel);

        //button
        JButton go = new JButton("Go");

        //calling action listener
        go.addActionListener(new ActionListenerGoButton(funcField, xminField, xmaxField, yminField, ymaxField, graphPanel));

        //panel for button
        JPanel panel2 = new JPanel();
        panel2.setLayout(new FlowLayout());
        panel2.add(go);
        window.add(panel2);

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setVisible(true);
    }
    public static void main(String[] args) {
        GraphCalc theWindow = new GraphCalc();
    }
}