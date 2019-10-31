/**
 * @author Tuan Nguyen
 * @since 20191031
 * @description
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
 */
public class SortByReverse {
    /** sort an array using reverse(lst, i, j) */
    public int[] sort(int[] arr) {
        int n = arr.length;
        int slideMinIndex;
        // trivial case
        if (n <= 1)     
            return arr;
        // other cases
        for (int i = 0; i < n; i++) {
            slideMinIndex = slideMinIndex(arr, i, n);
            reverse(arr, i, slideMinIndex);
        }
        return arr;
    }

    /** reverse all elements in array from index i to j */
    private void reverse(int[] arr, int i, int j) {
        while (i <= j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    /** return the index of min element from array from index i to j */
    private int slideMinIndex(int[] arr, int i, int j) {
        int index = i;
        int min = arr[i];
        for (int k = i+1; k <= j; k++) {
            if (arr[k] < min) {
                min = arr[k];
                index = k;
            }
        }
        return index;
    }

    public static void main(String[] args) {
        SortByReverse s = new SortByReverse();
        int[] arr;
        // test 1
        arr = new int[]{5,4,3,2,1};
        assert(s.sort(arr) == new int[]{1,2,3,4,5});
        // test 2
        arr = new int[]{0};
        assert(s.sort(arr) == new int[]{0});
    }
}