/**
 * @author Tuan Nguyen
 * @since 20191110
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
 */
public class EditDistance {
    /** return min no. characters to change x into y */
    public int minEditDistance(String x, String y) {
        int n = x.length();
        int m = y.length();
        int[][] d = new int[n][m];
        // trivial cases
        if (n == 0) // x is empty    
            return m;
        if (m == 0) // y is empty
            return n;
        // base case
        if (x.charAt(0) == y.charAt(0)) // no difference btw 1st character of x & y
            d[0][0] = 0;
        else
            d[0][0] = 1;
        // dynamic programming: d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+0/1)
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0)   // skip d[0][0] as already base case
                    continue;
                else if (i == 0 && j != 0)  // 1st row
                    d[i][j] = d[i][j-1] + 1;
                else if (i != 0 && j == 0)  // 1st column
                    d[i][j] = d[i-1][j] + 1;
                else {
                    int insertCost = d[i-1][j] + 1;
                    int deleteCost = d[i][j-1] + 1;
                    int substituteCost = (x.charAt(i) == y.charAt(j)) ? d[i-1][j-1] : d[i-1][j-1] + 1;
                    d[i][j] = Math.min(substituteCost, Math.min(insertCost, deleteCost));
                }

            }
        }
        return d[n-1][m-1];
    }

    public static void main(String[] args) {
        EditDistance ed = new EditDistance();
        String x, y;
        // test 1
        x = "kitten";
        y = "sitting";
        assert(ed.minEditDistance(x, y) == 3);
        // test 2
        x = "Hello";
        y = "Jello";
        assert(ed.minEditDistance(x, y) == 1);
        // test 3
        x = "good";
        y = "goodbye";
        assert(ed.minEditDistance(x, y) == 3);
    }
}