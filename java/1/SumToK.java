import java.util.Arrays;
/**
 * @author Tuan Nguyen
 * @since 20191030
 * @description
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
 */
public class SumToK {
    /** return true any two numbers from the list add up to k */
    public boolean sumToK(int[] arr, int k) {
        int n = arr.length;
        int l = 0;
        int r = n - 1;

        Arrays.sort(arr);   // running time: O(n*log n)
        
        while (l < r) {     // running time: O(n)
            if (arr[l] + arr[r] == k)
                return true;
            else if (arr[l] + arr[r] < k)
                l++;
            else    // sum > k
                r--;
        }
        return false;   // reach this, then no pair sums to k
    }

    public static void main(String[] args) {
        SumToK s = new SumToK();
        int[] arr;
        int k;
        // test 1
        arr = new int[]{10,15,3,7};
        k = 17;
        assert(s.sumToK(arr, k) == true);
        // test 2
        arr = new int[]{10,15,3,7};
        k = 0;
        assert(s.sumToK(arr, k) == false);
    }
}