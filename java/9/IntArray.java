import java.util.Arrays;

/**
 * @author Tuan Nguyen
 * @since 20191102
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
 */
public class IntArray {
    /** returns the largest sum of non-adjacent numbers */
    public int maxSum_NonAdjacentNumbers(int[] arr) {
        int n = arr.length;
        int[] sum = new int[n];
        if (n == 0)             // trivial cases
            return 0;
        else if (n == 1)
            return arr[0];
        else if (n == 2)
            return Math.max(arr[0], arr[1]);
        else {
            sum[0] = arr[0];
            sum[1] = arr[1];
            for (int j = 2; j < n; j++) {   // dynamic programming: find local sum at each index
                int[] slice = Arrays.copyOfRange(arr, 0, j-2);
                sum[j] = arr[j] + max(slice);
            }
            return max(sum);
        }
    }

    /** return the max element in array */
    public int max(int[] arr) {
        int n = arr.length;
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max)
                max = arr[i];
        }
        return max;
    }

    public static void main(String[] args) {
        IntArray ia = new IntArray();
        int[] arr;
        // test 1
        arr = new int[]{2,4,6,2,5};
        assert(ia.maxSum_NonAdjacentNumbers(arr) == 13);
        // test 2
        arr = new int[]{5,1,1,5};
        assert(ia.maxSum_NonAdjacentNumbers(arr) == 10);
    }
}