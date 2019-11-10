import java.util.Arrays;

/**
 * @author Tuan Nguyen
 * @since 20191110
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
 */
public class Median {
    /** print out the median of the list so far on each new element */
    public void printRunningMedian(int[] arr) {
        int n = arr.length;
        for (int i = 1; i <= n; i++) {
            int[] runningArray = Arrays.copyOfRange(arr, 0, i);
            System.out.println(median(runningArray));
        }
    }
    /** return the median of a given array */
    public double median(int[] arr) {
        int n = arr.length;
        if (n == 0)         // trivial case: empty array
            return 0;
        else if (n == 1)    // trivial case: 1-element array
            return arr[0];
        else {
            Arrays.sort(arr);
            if (n % 2 == 1)         // odd-length array
                return arr[n/2];    // return middle element
            else                    // even-length array
                return (arr[n/2] + arr[n/2 - 1]) / 2.0; // median = average of 2 middle numbers
        }
    }

    public static void main(String[] args) {
        Median m = new Median();
        int[] arr;
        // test 1
        arr = new int[]{2, 1, 5, 7, 2, 0, 5};
        m.printRunningMedian(arr);  // 2 1.5 2 3.5 2 2 2
    }
}