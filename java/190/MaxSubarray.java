/**
 * @author Tuan Nguyen
 * @since 20191123
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
 */
public class MaxSubarray {
    /** return max subarray sum from a circular array */
    public int maxCircularSubarraySum(int[] arr) {
        // max subarray sum in 1-way
        int maxKadane = kadane(arr);
        // find max subarray sum in circular array
        int n = arr.length;
        int[] inverted = new int[n];    // array of all elements are opposite-valued from input array
        int arrSum = 0;
        for (int i = 0; i < n; i++) {
            arrSum += arr[i];
            inverted[i] = -arr[i];
        }
        int nonWrap = kadane(inverted); // find non-wrap sum, i.e max subarray sum from inverted array

        return (maxKadane > arrSum + nonWrap) ? maxKadane : arrSum + nonWrap;
    }
    
    /** return max subarray sum in an array */
    public int kadane(int[] arr) {
        int maxSum = 0;
        int curSum = 0;
        for (int i : arr) {
            if (curSum < 0) // reset current sum
                curSum = 0;
            curSum += i;
            if (curSum > maxSum)    // update max sum if possible
                maxSum = curSum;
        }
        return maxSum;
    }

    public static void main(String[] args) {
        MaxSubarray ms = new MaxSubarray();
        int[] arr;
        // test 1
        arr = new int[]{8, -1, 3, 4};
        assert(ms.maxCircularSubarraySum(arr) == 15);
        // test 2
        arr = new int[]{-4, 5, 1, 0};
        assert(ms.maxCircularSubarraySum(arr) == 6);
    }
}