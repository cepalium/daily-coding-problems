/**
 * @author Tuan Nguyen
 * @since 20190918
 * @description
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
 */
public class IntersectLinkedList<E> {
    // --------- nested Node class -----------
    public static class Node<E> {
        // instace variables
        private E element;
        private Node<E> next;
        // constructor
        private Node(E e, Node<E> n) {
            element = e;
            next = n;
        }
        // accessors
        private E getElement() { return element; }
        private Node<E> getNext() { return next; }
        // update methods
        private void setNext(Node<E> n) { next = n; }
    } // ------ end of nested Node class ---------

    /** Java implemenation of SinglyLinkedList class */
    public static class SinglyLinkedList<E> {
        // instance variables
        private Node<E> head = null;
        private Node<E> tail = null;
        private int size = 0;
        // constructor
        public SinglyLinkedList() { }
        // access methods
        public int size() { return size; }
        public boolean isEmpty() { return size == 0; }
        /** return 1st element of linked list*/
        public E first() {
            if (isEmpty()) return null;
            return head.getElement();
        }
        /** return last element of linked list*/
        public E last() {
            if (isEmpty()) return null;
            return tail.getElement();
        }
        /** return 1st node of linked list */
        public Node<E> getFirst() {
            if (isEmpty()) return null;
            return head;
        }
        // update methods
        /** add element e to front of linked list */
        public void addFirst(E e) {
            head = new Node<>(e, head);
            if (isEmpty())
                tail = head;
            size++;
        }
        /** add element e to end of linked list */
        public void addLast(E e) {
            Node<E> newest = new Node<>(e, null);
            if (isEmpty())
                head = newest;
            else
                tail.setNext(newest);
            tail = newest;
            size++;
        }
        /** remove and return the 1st element of linked list */
        public E removeFirst() {
            if (isEmpty()) return null;
            E answer = head.getElement();
            head = head.getNext();
            size--;
            if (size == 0)
                tail = null;
            return answer;
        }
    }

    // constructor
    public IntersectLinkedList() { }

    /** return the 1st intersected element of 2 linked lists (null if no such node exists)
     * condition: the intersected node in both 2 lists is the same
     * therefore, the following nodes after the 1st intersected node are the same for both lists, too
     * @running time: O(M+N), where M and N are the lengths of the 2 input lists respectively
     */
    public E intersect(SinglyLinkedList<E> l1, SinglyLinkedList<E> l2) {
        int minSize = Math.min(l1.size(), l2.size());   // check the size of smaller linked list
        // move the current node of 2 linked list to the same position w.r.t last node
        Node<E> l1cur = l1.getFirst();
        if (l1.size() - minSize > 0) {
            for (int k=0; k < l1.size() - minSize; k++)
                l1cur = l1cur.getNext();
        }
        Node<E> l2cur = l2.getFirst();
        if (l2.size() - minSize > 0) {
            for (int k=0; k < l2.size() - minSize; k++)
                l2cur = l2cur.getNext();
        }
        // check if current nodes from both lists are the same
        // if not, move the current node to its next node
        while (l1cur != null && l2cur != null) {
            if (l1cur.getElement() == l2cur.getElement())
                return l1cur.getElement();
            l1cur = l1cur.getNext();
            l2cur = l2cur.getNext();
        }
        return null;    // no intersected node if reach this
    }
    
    // main method
    public static void main(String[] args) {
        IntersectLinkedList<Integer> intersectList = new IntersectLinkedList<>();
        SinglyLinkedList<Integer> list1 = new SinglyLinkedList<>();
        SinglyLinkedList<Integer> list2 = new SinglyLinkedList<>();
        list1.addLast(3);
        list1.addLast(7);
        list1.addLast(8);
        list1.addLast(10);
        list2.addLast(99);
        list2.addLast(1);
        list2.addLast(8);
        list2.addLast(10);
        Integer intersectNode = intersectList.intersect(list1, list2);
        System.out.println(intersectNode);  // print 8
    }
}