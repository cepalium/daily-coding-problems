/**
 * @author Tuan Nguyen
 * @since 20190912
 */
/**
 * Given the head of a singly linked list, reverse it in-place.
 */
public class ReverseLinkedList {
    public static class SinglyLinkedList<E> {
        // ------- nested class Node -------------
        private class Node<E> {
            // instance variables of class Node
            E element;
            Node<E> next;
            // constructor
            private Node(E e, Node<E> n) {
                element = e;
                next = n;
            }
            // access methods
            public E getElement() { return element; }
            public Node<E> getNext() { return next; }
            // update method
            public void setNext(Node<E> n) { next = n; }
        } // ----- end of nested class Node -------

        // instance variable of class LinkedList
        private Node<E> head = new Node<>(null, null);
        private Node<E> tail = new Node<>(null, null);
        private int size = 0;
        // access methods
        public int size() { return size; }
        public boolean isEmpty() { return size == 0; }
        public E first() {
            if (isEmpty()) return null;
            return head.getElement();
        }
        public E last() {
            if (isEmpty()) return null;
            return tail.getElement();
        }
        /** print linked list s.t each element are separated by 1 space */
        public void printLinkedList() {
            Node<E> node = head;
            for (int j=0; j<size; j++) {
                System.out.print(node.getElement() + " ");
                node = node.getNext();
            }
            System.out.println();
        }
        // update methods
        /** add element e to front of list */
        public void addFirst(E e) {
            Node<E> newest = new Node<>(e, head);
            head = newest;
            if (size == 0)
                tail = head;    // link tail to head itself
            size++;
        }
        /** add element e to last of list */
        public void addLast(E e) {
            Node<E> newest = new Node<>(e, null);
            if (isEmpty())
                head = newest;  // special case: empty list
            else
                tail.setNext(newest);
            tail = newest;
            size++;
        }
        /** */
        public E removeFirst() throws IllegalStateException {
            if (isEmpty()) return null;
            Node<E> answer = head;
            head = head.getNext();
            size--;
            return answer.getElement();
        }
        // new update method: reverse linked list
        public void reverse() {
            Node<E> prevHead = new Node<>(null, null);  // before-head node initialized
            Node<E> afterHead = head.getNext();         // after-head node initialized
            for (int j=0; j<size; j++) {  // go through 0-th to n-th element
                if (j == 0)         // after reversing, head is tail
                    tail = head;    // then, set 1st head to be tail
                head.setNext(prevHead); // reverse
                prevHead = head;
                if (j < size -1) {      // update head node & node after head only when after-head node is the last node of list
                    head = afterHead;               // shift nodes to left
                    afterHead = head.getNext();
                }
            }
        }
    }

    // main method
    public static void main(String[] args) {
        SinglyLinkedList<Integer> l = new SinglyLinkedList<>();
        l.addFirst(1);
        l.addFirst(2);
        l.addFirst(3);
        l.printLinkedList();
        l.reverse();
        l.printLinkedList();
        System.out.println(l.first());
        System.out.println(l.last());
    }
}