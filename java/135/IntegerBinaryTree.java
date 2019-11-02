import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author Tuan Nguyen
 * @since 20191102
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
 */
/** a linked-node implementation for binary tree */
public class IntegerBinaryTree {

    /** lightweight structure for storing tree node */
    protected class Node {
        // instance variables of Node
        int element;
        Node parent;
        Node left;
        Node right;
        int pathSum;    // path sum from root to this node
        
        // constructor
        Node(int e, Node p, Node l, Node r) {
            element = e;
            parent = p;
            left = l;
            right = r;
        }
        
        // getters & setters
        int getElement() { return element; }
        void setElement(int e) { element = e; }
        Node getParent() { return parent; }
        void setParent(Node p) { parent = p; }
        Node getLeft() { return left; }
        void setLeft(Node l) { left = l; }
        Node getRight() { return right; }
        void setRight(Node r) { right = r; }
        int getPathSum() { return pathSum; }
        void setPathSum(int ps) { pathSum = ps; }
    } // ----- end of nested Node class -----

    // instance variables of BinaryTree
    Node root;
    int size;
    List<Integer> pathSums = new ArrayList<>(); // list of path sums from root to all leaves
    
    // create an empty tree
    public IntegerBinaryTree() {
        root = null;
        size = 0;
    }
    
    // public accessors
    public int length() { return size; }
    public boolean isEmpty() { return size == 0;}
    public Node root() { return root; }
    public Node parent(Node n) { return n.getParent(); }
    public Node left(Node n) { return n.getLeft(); }
    public Node right(Node n) { return n.getRight(); }
    public Iterable<Node> children(Node n) {
        List<Node> snapshot = new ArrayList<>(2);
        if (left(n) != null)
            snapshot.add(left(n));
        if (right(n) != null)
            snapshot.add(right(n));
        return snapshot;
    }
    public int numChildren(Node n) {
        int counter = 0;
        if (left(n) != null)
            counter++;
        if (right(n) != null)
            counter++;
        return counter;
    }
    public boolean isRoot(Node n) { return n == root; }
    public boolean isLeaf(Node n) { return numChildren(n) == 0; }
    
    // public update methods
    /** add e as root and return new node */
    public Node addRoot(int e) {
        if (!isEmpty())
            throw new IllegalArgumentException("Root exists");
        root = new Node(e, null, null, null);
        size = 1;
        return root;
    }
    /** add e as left child of Node n and return new node */
    public Node addLeft(Node n, int e) {
        if (left(n) != null)
            throw new IllegalArgumentException("Left child exists");
        Node newest = new Node(e, n, null, null);
        n.setLeft(newest);
        size++;
        return newest;
    }
    /** add e as right child of Node n and return new node */
    public Node addRight(Node n, int e) {
        if (right(n) != null)
            throw new IllegalArgumentException("Right child exists");
        Node newest = new Node(e, n, null, null);
        n.setRight(newest);
        size++;
        return newest;
    }

    /** return the minimum path sum from root to leaves */
    public int minimumPathSum() {
        if (isEmpty())
            throw new IllegalArgumentException("Empty tree");
        subTree_minimumPathSum(root());
        return Collections.min(pathSums);
    }
    /** generate the path sum from root to leaves by preorder traversal */
    private void subTree_minimumPathSum(Node n) {
        if (isLeaf(n)) {
            int leafSum = n.getElement() + parent(n).getPathSum();
            pathSums.add(leafSum);
        } else {
            for (Node c: children(n))
                subTree_minimumPathSum(c);
        }
    }

    public static void main(String[] args) {
        IntegerBinaryTree T = new IntegerBinaryTree();
        Node r = T.addRoot(10);
        Node lr = T.addLeft(r, 5);
        Node rr = T.addRight(r, 5);
        Node rlr = T.addRight(lr, 2);
        Node rrr = T.addRight(rr, 1);
        Node lrrr = T.addLeft(rrr, -1);
        assert(T.minimumPathSum() == 15);
    }
}