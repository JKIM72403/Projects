/**
 * Interpreter.java
 *
 * Class to generate ExprNode trees based on a given
 * input.
 *
 * @author Jonathan Kim
 * CSCI 235, Wheaton College, Spring 2023
 * Project 7
 *
 * Date? April 27, 2023
 */

public class Interpreter {
    /**
     * Turn a string into an ExprNode tree.
     *
     * @param input The string to parse
     * @return The root of the ExprNode tree
     */
    // I referred to the lab
    public static ExprNode parse(String input) {
        String[] nodes = ExprStringSlicer.slice(input);
        if (nodes.length == 1) {
            // base case: node is a Number or Variable
            if (nodes[0].equals("x")){
                return new Variable();
            } else {
                return new Number(nodes[0]);
            }
        } else {
            //recursive case: node is an Operation
            ExprNode left = parse(nodes[0]);
            String operator = nodes[1];
            ExprNode right = parse(nodes[2]);
            return new Operation(operator, left, right);
        }
    }


    /**
     * For testing project 7 (Part A).
     */
    public static void main(String[] args) {
        ExprNode tree = parse(args[0]);
        System.out.println(tree.evaluate(Double.parseDouble(args[1])));
    }


}
