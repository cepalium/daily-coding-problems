import java.util.Arrays;

/**
 * @author Tuan Nguyen
 * @since 20191026
 * @desription
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
 */
public class FindDuplicate {
    /** find the duplicate int from an array of length n+1 whose eleemnts in the set {1,2,...,n} */
    public int findDuplicate(int[] arr) {
        int n = arr.length - 1;                  // max range n of input array
        int expected_sum = n * (n+1) / 2;
        int real_sum = Arrays.stream(arr).sum();  // sum all elements in input array
        return real_sum - expected_sum;         // the duplicate element
    }

    public static void main(String[] args) {
        FindDuplicate fd = new FindDuplicate();
        int[] a;
        // test 1
        a = new int[]{1,1,2,3,4,5};
        assert(fd.findDuplicate(a) == 1);
        // test 2
        a = new int[]{1,2,3,3,4,5,6};
        assert(fd.findDuplicate(a) == 3);
    }
}