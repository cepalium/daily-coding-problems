/**
 * @author Tuan Nguyen
 * @since 20191102
Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?
 */
public class Rotation {
    /** rotates a list by k elements */
    public void rorate(int[] arr, int k) {
        int n = arr.length;
        for (int i = 0; i < k; i++) {       // rorate by k times
            for (int j = 0; j < n-1; j++)   // make first element to last of array by swapping
                swap(arr[j], arr[j+1]);
        }
    }

    /** swap a to b & b to a */
    private void swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    public static void main(String[] args) {
        Rotation r = new Rotation();
        int[] arr;
        int k;
        // test 1
        arr = new int[]{1,2,3,4,5};
        k = 2;
        r.rorate(arr, k);
        assert(arr == new int[]{3,4,5,1,2});
    }
}