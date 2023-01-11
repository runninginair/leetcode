''' 25. Reverse Nodes in k-Group
Hard       9468     545     Add to List     Share
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:    The number of nodes in the list is n.
                1 <= k <= n <= 5000
                0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?

Accepted:         614,811
Submissions:    1,150,111
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self,head) -> str:
        if not head: return 'None'
        return str(head.val) + " -> " + self.toString(head.next)

class Solution:
    def reverseList(self, head, k):
        prev, curr, tail = None, head, head
        while k > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        tail.next = None
        return prev, tail

    def reverseKGroup(self, head, k: int):
        if not head:
            return None

        # init two pointers, p1, p2, 
        p1 = p2 = head
        step = k
        while step > 0:
            p2 = p2.next
            if p2 is None: return p1
            step -= 1
            
        new_head, tail = self.reverseList(p1, k)
        # tail.next = p2
        tail.next = self.reverseKGroup(p2, k)

        return new_head
                
    


def main():
    sol = Solution()

    n1, n2, n3, n4, n5, n6, n7 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6), ListNode(7)
    n1.next, n2.next, n3.next, n4.next, n5.next, n6.next = n2, n3, n4, n5, n6, n7
    print(n1.toString(n1))
    new_LL =sol.reverseKGroup(n1, 3)
    print(n1.toString(new_LL))    

    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    print(n1.toString(n1))
    new_LL =sol.reverseKGroup(n1, 2)
    print(n1.toString(new_LL))    

    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next, n2.next = n2, n3
    print(n1.toString(n1))
    new_LL =sol.reverseKGroup(n1, 3)
    print(n1.toString(new_LL))    

main()