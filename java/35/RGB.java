/**
 * @author Tuan Nguyen
 * @since 20191110
Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
 */
public class RGB {
    /** segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last */
    public void arrangeRGB(char[] arr) {
        int n = arr.length;
        int l = 0, r = n-1;
        while (l < r) { // arrange 'R' to first 
            if (arr[r] == 'R' && arr[l] != 'R') {
                char temp = arr[r]; // swap char at l & r
                arr[r] = arr[l];
                arr[l] = temp;
                l++; r--;   // update pivots
            } else
                r--;
        }
        l = 0; r = n-1; // reset pivots for next looping
        while (l < r) { // arrange 'B' to last
            if (arr[l] == 'B' && arr[r] != 'B') {
                char temp = arr[r]; // swap char at l & r
                arr[r] = arr[l];
                arr[l] = temp;
                l++; r--;   // update pivots
            } else
                l++;
        }
    }

    public static void main(String[] args) {
        RGB rgb = new RGB();
        char[] arr;
        // test 1
        arr = new char[]{'G', 'B', 'R', 'R', 'B', 'R', 'G'};
        rgb.arrangeRGB(arr);
        assert(arr == new char[]{'R', 'R', 'R', 'G', 'G', 'B', 'B'});
    }
}