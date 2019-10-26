/**
 * @author Tuan Nguyen
 * @since 20191025
 * description
Given an array of integers, return a new array where each element in the new array 
is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
 */
public class SmallerElementsToRight {
    /** return a new array where each element in the new array 
    is the number of smaller elements to the right of that element in the original input array*/
    public int[] smallerElementsToRight(int[] arr) {
        int n = arr.length;
        int[] smallerElements = new int[n];
        for (int i = 0; i < n; i++) {           // for each element 
            int counter = 0;
            for (int j = i+1; j < n; j++) {     // iteratively count no. smaller elements to its right
                if (arr[i] > arr[j])
                    counter++;
            }
            smallerElements[i] = counter;
        }
        return smallerElements;
    }

    public static void main(String[] args) {
        SmallerElementsToRight ser = new SmallerElementsToRight();
        int[] arr;
        // test 1
        arr = new int[]{3,4,9,6,1};
        assert(ser.smallerElementsToRight(arr) == new int[]{1,1,2,1,0});
        // test 2
        arr = new int[]{5,4,3,2,1};
        assert(ser.smallerElementsToRight(arr) == new int[]{4,3,2,1,0});
    }
}