import java.util.ArrayDeque;
import java.util.Stack;

/**
 * @author Tuan Nguyen
 * @since 20191110
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. 
This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
 */
public class InterleavedStack {
    /** interleave the first half of the stack with the second half reversed using only one other queue */
    public void interleavedStack(Stack<Integer> stack) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int n = stack.size();
        for (int i = 0; i < n; i++) {
            while (stack.size() > i + 1)
                queue.addFirst(stack.pop());
            while (!queue.isEmpty())
                stack.push(queue.pollLast());
        }
    }

    public static void main(String[] args) {
        InterleavedStack is = new InterleavedStack();
        Stack<Integer> stack;
        // test 1
        stack = new Stack<>();
        for (int i = 1; i < 6; i++)
            stack.push(i);
        System.out.println("Before: " + stack);   // 1,2,3,4,5
        is.interleavedStack(stack);
        System.out.println("After: " + stack);   // 1,5,2,4,3

        // test 2
        stack = new Stack<>();
        for (int i = 1; i < 5; i++)
            stack.push(i);
        System.out.println("Before: " + stack);   // 1,2,3,4
        is.interleavedStack(stack);
        System.out.println("After: " + stack);   // 1,4,2,3
    }
}