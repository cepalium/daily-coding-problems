/**
 * @author Tuan Nguyen
 * @since 20191110
Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
 */
public class Hopping {
    /** return true if you can reach to the last index starting at index 0 */
    public boolean isLastReachable(int[] hops) {
        int n = hops.length;
        int i = 0;              // start from index 0
        while (hops[i] != 0)  // hop until 0 jump-step, i.e stop hopping
            i = (i + hops[i]) % n;
        if (i != n-1)   // current position not match the last index
            return false;
        else
            return true;    // current position is last index
    }

    public static void main(String[] args) {
        Hopping h = new Hopping();
        int[] hops;
        // test 1
        hops = new int[]{2,0,1,0};
        assert(h.isLastReachable(hops) == true);
        // test 2
        hops = new int[]{1,1,0,1};
        assert(h.isLastReachable(hops) == false);
    }
}