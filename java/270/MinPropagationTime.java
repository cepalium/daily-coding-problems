/**
    @author Tuan nguyen
    @since 20200208
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b. Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
*/
import java.util.Arrays;

public class MinPropagationTime {
    /* return the min time to propagate a msg from node 0 to all */
    public int minProgapationTime(int N, int[][] edges) {
        int[] prop = new int[N+1];
        Arrays.fill(prop, -1);
        prop[0] = 0;
        int num_edges = edges.length;
        for (int i = 0; i < num_edges; i++) {
            int a = edges[i][0], b = edges[i][1], t = edges[i][2];
            int t_a = prop[a], t_b = prop[b];
            if ((t_b == -1) || (t_b > t_a + t))
            prop[b] = t_a + t;
        }
        return max(prop);
    }

    /* return max element in array */
    public int max(int[] arr) {
        int n = arr.length; 
        int max_num = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max_num)
                max_num = arr[i];
        }
        return max_num;
    }

    public static void main(String[] args) {
        MinPropagationTime mpt = new MinPropagationTime();
        int N = 5;
        int[][] edges = {{0, 1, 5}, {0, 2, 3}, {0, 5, 4}, {1, 3, 8}, {2, 3, 1}, {3, 5, 10}, {3, 4, 5}};
        assert mpt.minProgapationTime(5, edges) == 9;
    }
}