/**
 * @author Tuan Nguyen
 * @since 20191031
 * @description
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x Ordering within a part can be arbitrary.
For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]
 */
public class Partition {
    /** return an array s.t 1st part < x, 2nd part = x, 3rd part > x */
    public int[] partition(int[] arr, int x) {
        int n = arr.length;
        if (n <= 1)     // trivial case
            return arr;
        int[] L = new int[n];
        int[] E = new int[n];
        int[] G = new int[n];
        int il=0, ie=0, ig=0, j=0;
        for (int i = 0; i < n; i++) {
            if (arr[i] < x)
                L[il++] = arr[i];
            else if (arr[i] == x)
                E[ie++] = arr[i];
            else
                G[ig++] = arr[i];
        }
        for (int k = 0; k < il; k++)
            arr[k] = L[k];
        for (int k = 0; k < ie; k++)
            arr[k+il] = E[k];
        for (int k =0; k < ig; k++)
            arr[k+il+ie] = G[k];
        return arr;
    }

    public static void main(String[] args) {
        Partition p = new Partition();
        int[] arr;
        int x;
        // test 1
        arr = new int[]{9, 12, 3, 5, 14, 10, 10};
        x = 10;
        assert(p.partition(arr, x) == new int[]{9, 3, 5, 10, 10, 12, 14});
    }
}