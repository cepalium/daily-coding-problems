import java.util.Stack;

/**
 * @author Tuan Nguyen
 * @since 20191110
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])", you should return true.

Given the string "([)]" or "((()", you should return false.
 */
public class ValidBrackets {
    /** return whether the brackets are balanced */
    public boolean isBracketsValid(String s) {
        final String open = "([{";
        final String close = ")]}";
        Stack<Character> stack = new Stack<>();
        for (char c: s.toCharArray()) {
            if (open.indexOf(c) != -1)  // opening bracket
                stack.push(c);
            else if (close.indexOf(c) != -1) {  // closing bracket
                if (stack.isEmpty())    // no opening bracket in stack
                    return false;
                if (close.indexOf(c) != open.indexOf(stack.pop()))  // not match btw closing and opening brackets
                    return false;
            }
        }
        return stack.isEmpty(); // if stack still has opening bracket, then it is not balanced
    }

    public static void main(String[] args) {
        ValidBrackets vb = new ValidBrackets();
        String s;
        // test 1
        s = "([])";
        assert(vb.isBracketsValid(s) == true);
        // test 2
        s = "((()";
        assert(vb.isBracketsValid(s) == false);
    }
}