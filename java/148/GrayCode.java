/**
 * @author Tuan Nguyen
 * @since 20191027
 * @description
Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. 
Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
 */
public class GrayCode {
    /** generate all possible gray code for n-bit */
    public String[] generateGrayCode(int n) {
        if (n == 0)                 // trival cases n=0 & n=1
            return new String[]{};
        else if (n == 1)
            return new String[]{"0", "1"};
        else {
            String[] L1 = generateGrayCode(n-1);    // recursive calls
            String[] L2 = reverse(L1);
            for (String s: L1)  // add '0' before all codes in L1
                s = "0" + s;
            for (String s: L2)  // add '1' before all codes in L2
                s = "1" + s;
            String[] L = concat(L1, L2);    // resulting codes
            return L;
        }
    }

    /** return a new array which is the reverse of input array */
    private String[] reverse(String[] A) {
        int n = A.length;
        String[] B = new String[n];     // initialize B as reverse of A
        int left = 0;
        int right = n-1;
        while (left <= right) {     // copy A's left to B's right & A's right to B's left
            B[left] = A[right];
            B[right] = A[left];
            left++;                 // move cursors to middle
            right--;
        }
        return B;
    }

    /** return a new array which have elements from 2 input arrays */
    private String[] concat(String[] A, String[] B) {
        int na = A.length;
        int nb = B.length;
        String[] C = new String[na + nb];   // initialize array C having elements of A & B
        int nc = 0;
        for (String sa: A)  // copy elements in A into C
            C[nc] = sa;
            nc++;
        for (String sb: B)  // copy elements in B into C
            C[nc] = sb;
            nc++;
        return C;
    }

    public static void main(String[] args) {
        GrayCode gc = new GrayCode();
        int n;
        // test 1
        n = 1;
        assert(gc.generateGrayCode(n) == new String[]{"0", "1"});
        // test 2
        n = 2;
        assert(gc.generateGrayCode(n) == new String[]{"00", "01", "11", "10"});
    }
}