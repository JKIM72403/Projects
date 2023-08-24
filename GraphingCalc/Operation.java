/**
 * Operation.java
 *
 * A class for Operations.
 *
 * @author Jonathan Kim
 * Wheaton College, CSCI 235, Spring 2023
 * Project 7
 *
 * Date? April 27, 2023
 */
public class Operation implements ExprNode{
    /**
     * The operator, left, and right parts of the expression
     */
    private String operator;
    private ExprNode left;
    private ExprNode right;

    /**
     * Constructor.
     * @param text the text representation
     * @param leftOperand the left expression
     * @param rightOperand the right expression
     */
public Operation (String text, ExprNode leftOperand, ExprNode rightOperand){
        operator = text;
        left = leftOperand;
        right = rightOperand;
}

    /**
     * evaluate the operator expression
     * @return evaluate methods to fully evaluate the
     * expression
     */

    public double evaluate(double x){
        // switch to find operator
        switch(operator){
        case "+":
            return left.evaluate(x) + right.evaluate(x);
        case "-":
            return left.evaluate(x) - right.evaluate(x);
        case "*":
            return left.evaluate(x)*right.evaluate(x);
        case "^":
            return Math.pow(left.evaluate(x), right.evaluate(x));
        default:
            return left.evaluate(x)/right.evaluate(x);
}
    }

}
