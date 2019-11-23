import java.util.ArrayList;
import java.util.Set;

/**
 * @author Tuan Nguyen
 * @since 20191123
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], 
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
 */
public class LongestSubarray {
    /** return the length of longest subarray where all its elements are distinct */
    public int longestSubarrayLength(int[] arr) {
        ArrayList<Integer> set = new ArrayList<>();
        int maxLength = 0;
        for (int i : arr) {
            while (set.contains(i))     // find duplicate
                set.remove(0);          // pop 1st element in set
            set.add(i);
            if (set.size() > maxLength)
                maxLength = set.size();
        }
        return maxLength;
    }

    public static void main(String[] args) {
        LongestSubarray ls = new LongestSubarray();
        int[] arr;
        // test 1
        arr = new int[]{5, 1, 3, 5, 2, 3, 4, 1};
        assert(ls.longestSubarrayLength(arr) == 5);
    }
}