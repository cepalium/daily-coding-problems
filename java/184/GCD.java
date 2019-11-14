/**
 * @author Tuan Nguyen
 * @since 20191114
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
 */
public class GCD {
    /** return the greatest common denominator from array of n integers */
    public int gcdFromArray(int[] arr) {
        int n = arr.length;
        if (n == 0)
            return -1;
        else if (n == 1)
            return arr[0];
        else {
            int a = arr[0];
            for (int i = 1; i < n; i++) {
                int b = arr[i];
                a = gcd(Math.max(a, b), Math.min(a, b));
            }
            return a;
        }
    }
    /** return the greatest common demonimator from a & b, a>=b */
    public int gcd(int a, int b) {
        if (a < b)
            throw new IllegalArgumentException("a must be larger than b");
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    public static void main(String[] args) {
        GCD test = new GCD();
        int[] arr;
        // test 1
        arr = new int[]{42,56,14};
        assert(test.gcdFromArray(arr) == 14);
        // test 2
        arr = new int[]{3,6};
        assert(test.gcdFromArray(arr) == 3);
        // test 3
        arr = new int[]{1};
        assert(test.gcdFromArray(arr) == 1);
        // test 4
        arr = new int[]{};
        assert(test.gcdFromArray(arr) == -1);
    }
}