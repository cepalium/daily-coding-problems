/**
 * @author Tuan Nguyen
 * @since 20191110
You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
 */
public class MaxCoin {
    /** return maximum number of coins you can collect by the bottom right corner */
    public int maxCoin(int[][] coins) {
        int row = coins.length;
        int col = coins[0].length;
        int[][] accumulatedCoins = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == 0 || j == 0) // 1st row or 1st column
                    accumulatedCoins[i][j] = coins[i][j];   // base case
                else
                    accumulatedCoins[i][j] = coins[i][j] + Math.max(coins[i-1][j], coins[i][j-1]);  // Bellman's equation (dynamic programming)
            }
        }
        return accumulatedCoins[row-1][col-1];  // bottom right corner
    }

    public static void main(String[] args) {
        MaxCoin mc = new MaxCoin();
        int[][] coins;
        // test 1
        coins = new int[][]{{0,3,1,1},{2,0,0,4},{1,5,3,1}};
        assert(mc.maxCoin(coins) == 12);
    }
}