'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int val1 = 0;
        int val2 = 0;
        int hi = 0;
        int sum = 0;
        ListNode temp = new ListNode(0);
        ListNode result = temp;
        while(l1 != null || l2 != null || hi != 0){
            if(l1 != null){
                val1 = l1.val;
                l1 = l1.next;
            }
            else{
                val1 = 0;
            }
            if(l2 != null){
                val2 = l2.val;
                l2 = l2.next;
            }
            else{
                val2 = 0;
            }
            sum = val1+val2+hi;
            hi = sum/10;
            temp.next = new ListNode(sum%10);
            temp = temp.next;
        }
        return result.next;
    }
}
