/**
 * @author Tuan Nguyen
 * @since 20191123
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. 
You can advance at most, the number of steps that you're currently on. 
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
 */
public class Hopping {
    /** return True if the end of array is reachable from start */
    public boolean isEndReachable(int[] arr, int start) {
        int n = arr.length;
        boolean[] reachable = new boolean[n];   // array of each element's reachability
        reachable[start] = true;                // base case
        for (int i = start; i < n; i++) {
            if (reachable[i]) {
                for (int j = 1; j <= arr[i] && i + j < n; j++)  // dynamic programming: reachacble at most from current position
                    reachable[j] = true;
            }       
        }
        return reachable[n-1];  // true or false if last element is reachable
    }

    public static void main(String[] args) {
        Hopping h = new Hopping();
        int[] arr;
        // test 1
        arr = new int[]{1, 3, 1, 2, 0, 1};
        assert(h.isEndReachable(arr, 0) == true);
        // test 2
        arr = new int[]{1, 2, 1, 0, 0};
        assert(h.isEndReachable(arr, 0) == false);
    }
}