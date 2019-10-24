/**
 * @author Tuan Nguyen
 * @since 20190917
 * @description
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1
 */
import java.util.Arrays;

public class SumReversedLinkedList {
    // ----------- nested Node class -----------------
    protected static class Node {
        private Integer element;      // reference to element sotred at this node
        private Node next;   // reference to subsequent node in the list
        public Node(Integer e, Node n) {
            element = e;
            next = n;
        }
        public Integer getElement() { return element; }
        public Node getNext() { return next; }
        // update methods
        public void setElement(Integer e) { element = e;}
        public void setNext(Node n) { next = n; }
    } // --------------- end of nested Node class ---------------------

    public static class LinkedList {
        // instance variables of SinglyLinkedList
        private Node head = null;        // head node of list (null if empty)
        private Node tail = null;        // last node of list (null if empty)
        private int size = 0;
        public LinkedList() { }
        // access methods
        public int size() { return size; }
        public boolean isEmpty() { return size == 0; }
        public Integer first() {  // return, but not remove 1st element
            if (isEmpty()) return null;
            return head.getElement();
        }
        public Integer last() {
            if (isEmpty()) return null;
            return tail.getElement();
        }
        public Node getHead() {
            if (isEmpty()) return null;
            return head;
        }
        public Node getTail() {
            if (isEmpty()) return null;
            return tail;
        }
        /** */
        public String toString() {
            Integer[] arr = new Integer[size];
            Node cur = head;
            for (int k=0; k < size; k++) {
                arr[k] = cur.getElement();
                cur = cur.getNext();
            }
            return Arrays.toString(arr);
        }
        // update methods
        public void addFirst(Integer e) { // add element e to 1st of list
            head = new Node(e, head); // create and link a new node
            if (size == 0)
                tail = head;    // special case: new node becomes tail also
            size++;
        }
        public void addLast(Integer e) {  // add element e to last of list
            Node newest = new Node(e, null);   // node will be the tail
            if (isEmpty())
                head = newest;  // special case: previously empty list
            else
                tail.setNext(newest);   // new node after existing tail
            tail = newest;  // new node becomes tail
            size++;
        }
        public Integer removeFirst() {    // remove and return 1st element
            if (isEmpty()) return null; // nothing to remove
            Integer answer = head.getElement();
            head = head.getNext();  // will become null if list had only 1 node
            size--;
            if (size == 0)
                tail = null;    // special case: list is empty now
            return answer;
        }
    }

    // constructor
    public SumReversedLinkedList() { }

    /** sum another linked list to the current linked list object */
    public LinkedList sumLinkedList(LinkedList l1, LinkedList l2) {
        // instance variables
        LinkedList sumList = new LinkedList();
        Node l1cur = l1.getHead();
        Node l2cur = l2.getHead();      
        Integer l1Element;
        Integer l2Element;
        Integer carry = 0;
        Integer sum;
        while (l1cur != null || l2cur != null) {      // loop until both linked lists are running out of nodes
            if (l1cur != null)                    // if current list runs out of nodes, but the other list still has nodes
                l1Element = l1cur.getElement();  // then assign its value to 0
            else
                l1Element = 0;
            if (l2cur != null)                          // if the other list runs out of nodes, but the current list still has nodes
                l2Element = l2cur.getElement();          // then assign its value to 0
            else
                l2Element = 0;
            sum = l1Element + l2Element + carry;    // calculate the sum
            carry = 0;                              // reset the carry
            if (sum > 9) {                          // calculate the carry for next round
                carry = sum / 10;
                sum = sum % 10;
            }               
            // set the sum to current list          
            sumList.addLast(sum);
            // update next node if current node in list is not null
            if (l1cur != null)
                l1cur = l1cur.getNext();
            if (l2cur != null)
                l2cur = l2cur.getNext();
        }
        if (carry != 0)     // add carry as last node in linked list (if carry != 0)
            sumList.addLast(carry);
        return sumList;
    }

    public static void main(String[] args) {
        SumReversedLinkedList master = new SumReversedLinkedList();
        LinkedList list1 = new LinkedList();
        LinkedList list2 = new LinkedList();
        list1.addLast(9);
        list1.addLast(9);
        list2.addLast(5);
        list2.addLast(2);
        System.out.println(list1.toString());
        System.out.println(list2.toString());
        LinkedList sumList = master.sumLinkedList(list1, list2);
        System.out.println(sumList.toString());
    }
}