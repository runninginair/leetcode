''' 328. Odd Even Linked List
Medium      6.6K    401     Companies

Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:        The number of nodes in the linked list is in the range [0, 104].
                    -106 <= Node.val <= 106
Accepted:           617.9K
Submissions:        1M
Acceptance Rate:    60.3%

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res, cur = "", self
        while cur:
            res += str(cur.val) + " -> "
            cur = cur.next
        return res + "NULL"

        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
    
        oddptr = curr = head
        evenptr = even = head.next
        i = 1

        while curr:
            if i > 2:
                if i & 1:
                    oddptr.next = curr
                    oddptr = oddptr.next
                else:
                    evenptr.next = curr
                    evenptr = evenptr.next
            curr = curr.next
            i += 1
        evenptr.next = None
        oddptr.next = even

        return head

def main():
    sol = Solution()
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    print(n1)   # Input: head = [1,2,3,4,5]     # Output: [1,3,5,2,4]
    print(sol.oddEvenList(n1))

    l2, l1, l3, l5, l6, l4, l7 = ListNode(2), ListNode(1), ListNode(3), ListNode(5), ListNode(6), ListNode(4), ListNode(7)
    l2.next, l1.next, l3.next, l5.next, l6.next, l4.next = l1, l3, l5, l6, l4, l7
    print(l2)   # Input: head = [2,1,3,5,6,4,7]   # Output: [2,3,6,7,1,5,4]
    print(sol.oddEvenList(l2))

main()
