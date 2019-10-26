import java.util.Stack;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
/**
 * @author Tuan Nguyen
 * @since 20191026
 * @description
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, 
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
 */
public class ReversePolishNotation {
    /** return a double as evaluation of input expression in Reverse Polish Notation */
    public Double evaluateReversePolishNotation(String[] exp) {
        Stack<Double> stack = new Stack<>();        // stack initialized
        for (String s : exp) {                      // go through expression
            if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")) {     // operand in expression
                Double n1 = stack.pop();    // pop last 2 numbers in stack
                Double n2 = stack.pop();
                Double result = 0.0;
                switch (s) {                // calculate the small expression
                    case "+":
                        result = n2 + n1;
                        break;
                    case "-":
                        result = n2 - n1;
                        break;
                    case "*":
                        result = n2 * n1;
                        break;
                    case "/":
                        result = n2 / n1;
                        break;
                }
                stack.push(result);         // push the result into stack
            } else {
                stack.push(Double.parseDouble(s));  // push number in expression into stack
            }
        }
        return stack.pop();     // the last number in stack is the final result
    }

    public static void main(String[] args) {
        ReversePolishNotation rpn = new ReversePolishNotation();
        String[] exp;
        // test 1
        exp = new String[]{"15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"};
        assert(rpn.evaluateReversePolishNotation(exp) == 5);   
        // test 2
        exp = new String[]{"15", "7", "+"};
        assert(rpn.evaluateReversePolishNotation(exp) == 22);
    }
}