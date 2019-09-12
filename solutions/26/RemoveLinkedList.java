/**
 * @author Tuan Nguyen
 * @since 20190912
 */
/**
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
 */
public class RemoveLinkedList {
    public static class SinglyLinkedList<E> {
        // -------------- nested class Node -----------------
        private class Node<E> {
            // instance variables
            private E element;
            private Node<E> next;
            // constructor
            public Node(E e, Node<E> n) {
                element = e;
                next = n;
            }
            public E getElement() { return element; }
            public Node<E> getNext() { return next; }
            public void setNext(Node<E> n) { next = n; }
        } // ------- end of nested class Node ----------------
    
        // instace variables of LinkedList class
        private Node<E> head = new Node<>(null, null);
        private Node<E> tail = new Node<>(null, null);
        private int size = 0;
        // constructor
        public SinglyLinkedList() { }
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
                tail = head;
            size++;
        }
        /** add element e to last of list */
        public void addLast(E e){
            Node<E> newest = new Node<>(e, null);
            if (isEmpty())
                head = newest;
            else
                tail.setNext(newest);;
            tail = newest;
            size++;
        }
        /** remove and return 1st element in list */
        public E removeFirst() {
            Node<E> answer = head;
            head = head.getNext();
            size--;
            return answer.getElement();
        }
        /** remove and return k-th last element in list s.t k=0: tail, k = size-1: head */
        public E removeKthLastNode(int k) throws IllegalStateException {
            if (k < 0 || k > size)
                throw new IllegalStateException("Invalid input: " + k);
            if (k == size - 1)          // remove first
                return removeFirst();
            Node<E> prevNode = head;
            Node<E> answer = new Node<>(null, null);
            for (int j=size-1; j>=0; j--) {
                if (j == k) {                       // arrive at k-th last node of list
                    answer = prevNode.getNext();    // save the k-th last node
                    Node<E> afterNode = answer.getNext();
                    prevNode.setNext(afterNode);    // link previous node to k-th last node's next node
                    size--;
                    break;
                }
                else
                    prevNode = prevNode.getNext();  // move previous node to its next node
            }
            return answer.getElement();
        }
    }

    // main method
    public static void main(String[] args) {
        SinglyLinkedList<Integer> l = new SinglyLinkedList<>();
        l.addFirst(1);
        l.addFirst(2);
        l.addFirst(3);
        l.printLinkedList();
        l.removeKthLastNode(2);
        l.printLinkedList();
    }
}
