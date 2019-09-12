/**
 * @author Tuan Nguyen
 * @since 20190912
 */

/**
 * {@summary} 
 * Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
 * For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
 */
public class PalindromeDoublyLinkedList {
    public static class DoublyLinkedList<E> {
        // ------- nested class Node ---------
        private class Node<E> {
            // instance variables of class Node
            E element;
            Node<E> prev;
            Node<E> next;
            // constructor
            private Node(E e, Node<E> p, Node<E> n) {
                element = e;
                prev = p;
                next = n;
            }
            // access methods
            private E getElement() { return element; }
            private Node<E> getPrev() { return prev; }
            private Node<E> getNext() { return next; }
            // update methods
            private void setPrev(Node<E> p) { prev = p; }
            private void setNext(Node<E> n) { next = n; }
        } // ---------- end of nested class Node ---------

        // instance variables of class DoublyLinkedList
        private Node<E> header;
        private Node<E> trailer;
        private int size = 0;
        // constructor
        public DoublyLinkedList() {
            header = new Node<>(null, null, null);
            trailer = new Node<>(null, header, null);
            header.setNext(trailer);
        }
        // access methods
        public int size() { return size; }
        public boolean isEmpty() {return size == 0; }
        public E first() {
            if (isEmpty()) return null;
            return header.getNext().getElement();
        }
        public E last() {
            if (isEmpty()) return null;
            return trailer.getPrev().getElement();
        }
        public void printLinkedList() {
            Node<E> node = header.getNext();
            for (int j = 0; j < size; j++) {
                System.out.print(node.getElement() + " ");
                node = node.getNext();
            }
            System.out.println();
        }
        // update methods
        /** add element e to front of list*/
        public void addFirst(E e) {
            addBetween(e, header, header.getNext());
        }
        /** add element e to last of list*/
        public void addLast(E e) {
            addBetween(e, trailer.getPrev(), trailer);
        }
        /** remove & return 1st element in list */
        public E removeFirst() {
            if (isEmpty()) return null;
            return remove(header.getNext());
        }
        /** remove & return last element in list */
        public E removeLast() {
            if (isEmpty()) return null;
            return remove(trailer.getPrev());
        }
        // private update method
        /** add element e between before node and after node */
        private void addBetween(E e, Node<E> before, Node<E> after) {
            Node<E> newest = new Node<>(e, before, after);
            before.setNext(newest);
            after.setPrev(newest);
            size++;
        }
        /** remove and return element n */
        private E remove(Node<E> n) {
            Node<E> predecessor = n.getPrev();
            Node<E> successor = n.getNext();
            predecessor.setNext(successor);
            successor.setPrev(predecessor);
            size--;
            return n.getElement();
        }
        // new access method: check if this doubly linked list is palindrome
        /** return true if doubly linked list is palindrome, otherwise false */
        public boolean isPalindrome() {
            if (size < 2)   // base case: empty list or list of 1 element
                return true;
            Node<E> left = header.getNext();        // left node
            Node<E> right = trailer.getPrev();      // right node
            for (int j = 0; j < (int) size/2; j++) {    // left node and right node move toward middle position
                if (left.getElement() != right.getElement())    // if left node is different from right node
                    return false;                               // then, false
                else {  // else, move left node and right node toward middle 1 position
                    left = left.getNext();
                    right = right.getPrev();
                }
            }
            return true;    // doubly linked list is palindrome if reach this
        }
    }

    // main method
    public static void main(String[] args) {
        DoublyLinkedList<Integer> dList1 = new DoublyLinkedList<>();
        dList1.addFirst(1);
        dList1.addLast(4);
        dList1.addLast(3);
        dList1.addLast(4);
        dList1.addLast(1);
        dList1.printLinkedList();
        System.out.println("Is palindrome? " + dList1.isPalindrome());

        DoublyLinkedList<Integer> dList2 = new DoublyLinkedList<>();
        dList2.addFirst(1);
        dList2.addLast(4);
        dList2.printLinkedList();
        System.out.println("Is palindrome? " + dList2.isPalindrome());
    }
}