/**
 * ActionListenerGoButton.java
 *
 * Action listener for go button
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
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ActionListenerGoButton implements ActionListener, Painter {

    /**
     * The JTextFields and PaintPanel used
     */
    private JTextField funcField;
    private JTextField xminField;
    private JTextField xmaxField;
    private JTextField yminField;
    private JTextField ymaxField;
    private PaintPanel graphPanel;

    /**
     * Constructor.
     * @param funcField the function field
     * @param xminField the xmin field
     * @param xmaxField the xmax field
     * @param yminField the ymin field
     * @param ymaxField the ymax field
     * @param graphPanel the panel
     */

    public ActionListenerGoButton(JTextField funcField, JTextField xminField, JTextField xmaxField, JTextField yminField, JTextField ymaxField, PaintPanel graphPanel) {
        this.funcField = funcField;
        this.xminField = xminField;
        this.xmaxField = xmaxField;
        this.yminField = yminField;
        this.ymaxField = ymaxField;
        this.graphPanel = graphPanel;
    }

    /**
     * Button pressed
     */
    public void actionPerformed(ActionEvent e) {
        graphPanel.setPainter(this);
        /* Variables used in task 1
         * String function = funcField.getText();
         * double xmin;
         * double xmax;
         * double ymin;
         * double ymax;
         */

        try {
            /* Code used in task 1:
            * xmin = Double.parseDouble(xminField.getText());
            * xmax = Double.parseDouble(xmaxField.getText());
            * ymin = Double.parseDouble(yminField.getText());
            * ymax = Double.parseDouble(ymaxField.getText());
            * ExprNode tree = Interpreter.parse(function);
            * double valAtXMin = tree.evaluate(xmin);
            * double valAtXMax = tree.evaluate(xmax);
            * System.out.println("Function: " + function);
            * System.out.println("xmin: " + xmin);
            * System.out.println("xmax: " + xmax);
            * System.out.println("ymin: " + ymin);
            * System.out.println("ymax: " + ymax);
            * System.out.println("Function value at xmin: " + valAtXMin);
            * System.out.println("Function value at xmax: " + valAtXMax);
            */
            graphPanel.repaint();

        } catch (Exception e1) {
            System.out.println("An error occurred with the input. Try again.");
        }
    }

    /**
     * Update the display using the given graphics
     * object.
     * @param g The graphics object to manipulate
     */
    public void paint(Graphics g){

        //graph panel is 300 x 300
        String function = funcField.getText();

        //holds the inputted xmin value
        double xmin;

        //holds the inputted xmax value
        double xmax;

        //holds the inputted ymin value
        double ymin;

        //holds the inputted ymax value
        double ymax;

        //Getting inputted values and parsing as double
        xmin = Double.parseDouble(xminField.getText());
        xmax = Double.parseDouble(xmaxField.getText());
        ymin = Double.parseDouble(yminField.getText());
        ymax = Double.parseDouble(ymaxField.getText());

        //Interpreter class parse method on the function
        ExprNode tree = Interpreter.parse(function);

        //range values (found by subtracting largest by smallest)
        //xRange holds the range of inputted x values
        double xRange = xmax - xmin;

        //yRange holds the range of inputted y values
        double yRange = ymax - ymin;

        //calculated scale values:
        //300 is used because that is the size of the panel
        //xScale holds the scale of x
        double xScale = 300 / xRange;
        //yScale holds the scale of y
        double yScale = 300 / yRange;

        //AXIS LINES
        //Finding middle values for axis lines
        // and scaling them
        //xMiddle used for middle of x axis
        int xMiddle = (int) ((xmax + xmin)/2 * xScale);

        //yMiddle used for middle of y axis
        int yMiddle = (int) ((ymax + ymin)/2 * yScale);
        //if 0 is between xmin and xmax values
        if (0.0 >= xmin && 0.0 <= xmax) {
            // +150 to account for the offset of the panel itself
            // I used pixel values for these lines (0) and (300)
            g.drawLine(xMiddle + 150, 0, xMiddle + 150, 300);
        }
        //if 0 is between ymin and ymax values
        if (0.0 >= ymin && 0.0 <= ymax) {
            // +150 to account for the offset of the panel itself
            g.drawLine(0, yMiddle + 150, 300, yMiddle + 150);
        }

        //draw curve
        //Using xPixel instead of int i for clarity
        //for loop for each horizontal pixel
        for (int xPixel = 0; xPixel < 300; xPixel++) {
            //find the corresponding x value
            //by scaling the pixel and adding
            //the minimum x value
            double x = (xPixel / xScale) + xmin;
            //evaluate the function at the x value
            //using interpreter class
            double y = tree.evaluate(x);

            //check if the y value is within the y range
            if (y >= ymin && y <= ymax) {
                //finding correct y pixel value by scaling it
                //got help for this formula from cs help
                //session
                int yPixel = (int) ((ymax - y) * yScale);

                //making 1x1 pixel rectangle to draw expression
                g.fillRect(xPixel, yPixel, 1, 1);
            }
        }
    }
}