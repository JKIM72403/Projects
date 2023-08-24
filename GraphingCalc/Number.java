/**
 * Number.java
 *
 * A class for Number.
 *
 * @author Jonathan Kim
 * Wheaton College, CSCI 235, Spring 2023
 * Project 7
 *
 * Date? April 27, 2023
 */
public class Number implements ExprNode {

    /**
     * The value
     */
    private double value;

    /**
     * Constructor.
     * @param text The text to parse
     */
    public Number (String text) {
        value = Double.parseDouble(text);
    }

    /**
     * return/evaluate the value of the number
     * @return value: the value of the number
     */
    public double evaluate(double x){
        return value;
    }
}
