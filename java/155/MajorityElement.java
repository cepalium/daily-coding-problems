import java.util.HashMap;

/**
 * @author Tuan Nguyen
 * @since 20191027
 * @description
Given a list of elements, find the majority element, 
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
 */
public class MajorityElement {
    /** return the majority element which appears more than half the time */
    public int findMajorityElement(int[] arr) {
        int n = arr.length;
        int major = -1;
        HashMap<Integer, Integer> freq = new HashMap<>();   // map to store frequency of an element
        for (int k: arr) {                  // count frequecy for all elements
            if (freq.containsKey(k))
                freq.put(k, freq.get(k) + 1);
            else
                freq.put(k, 0);
        }
        for (int k: freq.keySet()) {    // find the majority element
            if (freq.get(k) >= n/2)
                major = k; 
        }
        return major;
    }

    public static void main(String[] args) {
        MajorityElement me = new MajorityElement();
        int[] arr;
        // test 1
        arr = new int[]{1,2,1,1,3,4,0};
        assert(me.findMajorityElement(arr) == 1);
        // test 2
        arr = new int[]{3,3,3,3,3,3,1,4,5,6,7,8};
        assert(me.findMajorityElement(arr) == 3);
    }
}