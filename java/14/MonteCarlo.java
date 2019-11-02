import java.util.Random;

/**
 * @author Tuan Nguyen
 * @since 20191102
The area of a circle is defined as πr2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
 */
public class MonteCarlo {
    /** return estimation of pi */
    public double piEstimation() {
        int n = 100000;
        int circlePoints = 0;
        double r = 1;
        double pi;
        for (int i = 0; i < n; i++) {
            double x = randRange(-r, r);
            double y = randRange(-r, r);
            if (x*x + y*y <= r*r)
                circlePoints++;
        }
        pi = 4.0 * circlePoints / n;
        return pi;
    }

    /** return a double between from & to */
    private double randRange(double from, double to) {
        Random r = new Random();
        return from + (to - from) * r.nextDouble();
    }

    public static void main(String[] args) {
        MonteCarlo mc = new MonteCarlo();
        System.out.println(mc.piEstimation());
    }
}