import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Tuan Nguyen
 * @since 20191110
Print the nodes in a binary tree level-wise. 
For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5
 */
public class BinaryTree<E> {
    /** a linked-node implementation for binary tree */
    // ----- nested Node class -----
    public static class Node<E> {
        /** a structure for storing tree node */
        protected E element;
        protected Node<E> parent;
        protected Node<E> right;
        protected Node<E> left;
        // constructor
        Node(E e, Node<E> p, Node<E> r, Node<E> l) {
            element = e;
            parent = p;
            right = r;
            left = l;
        }
        // getters & setters
        E getElement() { return element; }
        void setElement(E e) { element = e; }
        Node<E> getParent() { return parent; }
        void setParent(Node p) { parent = p; }
        Node<E> getLeft() { return left; }
        void setLeft(Node l) { left = l; }
        Node<E> getRight() { return right; }
        void setRight(Node r) { right = r; }
    } // ----- end of nested Node class

    protected Node<E> root;
    protected int size;
    // constructor: create an empty tree
    public BinaryTree() {
        root = null;
        size = 0;
    }
    // accessors
    public int size() { return size; }
    public boolean isEmpty() { return size == 0; }
    public Node<E> root() { return root; }
    public Node<E> parent(Node n) {
        if (n == root())
            return null;
        return n.getParent();
    }
    public Node<E> left(Node n) {
        return n.getLeft();
    }
    public Node<E> right(Node n) {
        return n.getRight();
    }
    public int numChildren(Node n) {
        int counter = 0;
        if (left(n) != null)
            counter++;
        if (right(n) != null)
            counter++;
        return counter;
    }
    public Iterable<Node<E>> children(Node n) {
        List<Node<E>> snapshot = new ArrayList<>(2);    // a node has max 2 children
        if (left(n) != null)
            snapshot.add(left(n));
        if (right(n) != null)
            snapshot.add(right(n));
        return snapshot;
    }
    /** Print the nodes in a binary tree level-wise */
    public void printBreadthFirst() {
        ArrayDeque<Node<E>> queue = new ArrayDeque<>();
        queue.addFirst(root());
        while (!queue.isEmpty()) {
            Node n = queue.pollFirst();
            System.out.print(n.getElement() + " ");
            for (Node c: children(n))
                queue.add(c);
        }
        System.out.println();
    }
    // public update methods
    public Node<E> addRoot(E e) {
        if (root() != null)
            throw new IllegalArgumentException("Root exists");
        root = new Node(e, null, null, null);
        size = 1;
        return root;
    }
    public Node<E> addLeft(Node n, E e) {
        if (left(n) != null)
            throw new IllegalArgumentException("Left child exists");
        Node<E> newest = new Node(e, n, null, null);
        n.setLeft(newest);
        size++;
        return newest;
    }
    public Node<E> addRight(Node n, E e) {
        if (right(n) != null)
            throw new IllegalArgumentException("Right child exists");
        Node<E> newest = new Node(e, n, null, null);
        n.setRight(newest);
        size++;
        return newest;
    }

    public static void main(String[] args) {
        BinaryTree<Integer> T = new BinaryTree<>();
        Node<Integer> a = T.addRoot(1);
        Node<Integer> l = T.addLeft(a, 2);
        Node<Integer> r = T.addRight(a, 3);
        Node<Integer> lr = T.addLeft(r, 4);
        Node<Integer> rr = T.addRight(r, 5);
        T.printBreadthFirst();  // 1,2,3,4,5 
    }
}