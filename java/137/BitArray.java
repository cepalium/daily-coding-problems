/**
 * @author Tuan Nguyen
 * @since 20191031
 * @description
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
 */
public class BitArray {
    final private int DEFAULT_CAPACITY = 1024;
    private int[] data;
    // constructor
    public BitArray() {
        data = new int[DEFAULT_CAPACITY];
    }
    public BitArray(int n) {
        data = new int[n];
    }
    // accessor
    public int get(int i) throws IndexOutOfBoundsException {
        if (i < 0 || i >= data.length)
            throw new IndexOutOfBoundsException("Invalid index: " + i);
        return data[i];
    }
    // update method
    public void set(int i, int val) throws IndexOutOfBoundsException, IllegalArgumentException {
        if (i < 0 || i >= data.length)
            throw new IndexOutOfBoundsException("Invalid index: " + i);
        if (val != 0 && val != 1)
            throw new IllegalArgumentException("Invalid value: " + val);
        data[i] = val;
    }

    public static void main(String[] args) {
        BitArray ba = new BitArray(10);
        assert(ba.get(0) == 0);
        ba.set(9, 1);
        assert(ba.get(9) == 1);
    }
}