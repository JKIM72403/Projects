/**
 * Variable.java
 *
 * An interface to define the operation evaluate() on
 * nodes in an expression tree.
 *
 * @author Jonathan Kim
 * Wheaton College, CSCI 235, Spring 2023
 * Project 7
 *
 * Date? April 27, 2023
 */

public class Variable implements ExprNode {
    /**
     * evaluate variable expression
     * @return x: the Variable expression
     */
    public double evaluate(double x) {
        return x;
    }
}