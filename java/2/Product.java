/**
 * @author Tuan Nguyen
 * @since 20191030
 * @description
Given an array of integers , return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, 
* if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]
* If our input was [3, 2, 1], the expected output would be [2, 3, 6]
 */
public class Product {
    /** return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i */
    public int[] productExceptItself(int[] arr) {
        int p = product(arr);
        int n = arr.length;
        int[] results = new int[n];
        for (int i = 0; i < n; i++)
            results[i] = p / arr[i];
        return results;
    }

    /** return the product from all elements in array */
    public int product(int[] arr) {
        int p = 1;
        for (int i: arr)
            p *= i;
        return p;
    }

    public static void main(String[] args) {
        Product p = new Product();
        int[] arr;
        // test 1
        arr = new int[]{1,2,3,4,5};
        assert(p.productExceptItself(arr) == new int[]{120,60,40,30,24});
        // test 2
        arr = new int[]{3,2,1};
        assert(p.productExceptItself(arr) == new int[]{3,2,1});
    }
}
