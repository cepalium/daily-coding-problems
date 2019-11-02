/**
 * @author Tuan Nguyen
 * @since 20191102
Given a real number n, find the square root of n. 
For example, given n = 9, return 3.
 */
public class Newton {
    /** return the square root of n */
    public double squareRoot(double n) {
        double x = 1;
        int noIterations = 10;
        for (int i = 0; i < noIterations; i++) {    // newton's method: x_n+1 = x_n - f(x_n) / f'(x_n)
            x = x - (x*x - n) / (2*x);              // f(x) = x^2 - n; f'(x) = 2x
        }
        return x;
    }

    public static void main(String[] args) {
        Newton newton = new Newton();
        int n;
        // test 1
        n = 9;
        System.out.println("Square root of " + n + " = " + newton.squareRoot(n));
        // test 2
        n = 2;
        System.out.println("Square root of " + n + " = " + newton.squareRoot(n));
    }
}