''' 24. Swap Nodes in Pairs

Medium      9.8K      368       Companies

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)


Example 1:      (1) -> (2) -> (3) -> (4) -> null

                (2) -> (1) -> (4) -> (3) -> null

Input: head = [1,2,3,4]
Output: [2,1,4,3]


Example 2:

Input: head = []
Output: []


Example 3:

Input: head = [1]
Output: [1]
 

Constraints:        The number of nodes in the list is in the range [0, 100].
                    0 <= Node.val <= 100
Accepted:           1.1M
Submissions:        1.8M
Acceptance Rate:    61.8%
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + " -> " + self.next.__str__()
        

class Solution:     # Neetcode Solution     T: O(n)     M: O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next

            # reverse the curr and curr.next pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # move pointers to next pair
            prev = curr
            curr = nxtPair

        return dummy.next

def main():
    sol = Solution()

    n4 = ListNode(4, None)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(n1)
    print(sol.swapPairs(n1))

if __name__ == "__main__":
    main()
