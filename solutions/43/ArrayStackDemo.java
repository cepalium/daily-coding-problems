import java.util.Arrays;

/**
 * @author Tuan Nguyen
 * @since 20190911
 */

/*
Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
 */
public class ArrayStackDemo {
    public static class ArrayStack {
        // instance variables
        private int capacity = 1024;
        private int size = 0;
        private int[] data;
        private int max;
        // constructors
        public ArrayStack() {
            data = new int[capacity];
        }
        // access methods
        public int size() { return size; }
        public boolean isEmpty() { return size == 0; }
        /** returns the maximum value in the stack currently */
        public int max() throws IllegalStateException { 
            if (size == 0)
                throw new IllegalStateException("Empty stack");
            return max;
        }
        /** returns stack as string */
        public String toString() {
            int[] d = new int[size];
            for (int k=0; k<size; k++)
                d[k] = data[k];
            return Arrays.toString(d);
        }
        // public update methods
        /** pushes an element onto the stack */
        public void push(int val) {
            if (size == capacity)
                resize(2*capacity);
            if (size == 0)
                max = val;
            else {
                if (val > max)
                    max = val;
            }
            data[size] = val;
            size++;
        }
        /** pops off and returns the topmost element of the stack */
        public int pop() throws IllegalStateException {
            if (size == 0)
                throw new IllegalStateException("Empty stack");
            int last = data[size-1];
            size--;
            return last;
        }
        // private update method: resize stack to have dynamic length
        private void resize(int c) {
            int[] temp = new int[c];
            for (int k=0; k<size; k++)
                temp[k] = data[k];
            data = temp;
        }
    }

    // main method
    public static void main(String[] args) {
        ArrayStack stack = new ArrayStack();
        stack.push(1);
        stack.push(3);
        stack.push(-1);
        System.out.println(stack.toString());
        System.out.println(stack.max());
        stack.pop();
        stack.pop();
        System.out.println(stack.toString());
    }
}
