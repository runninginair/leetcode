''' 142. Linked List Cycle II
Medium      9477      666      Add to List      Share

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected to
(0-indexed). It is -1 if there is no cycle.

Note that pos is not passed as a parameter.

Do not modify the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:    The number of the nodes in the list is in the range [0, 104].
                -105 <= Node.val <= 105
                pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?

Accepted:       872,274
Submissions:    1,877,338
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:   # Not work for infinite loop LinkedList.
        if not self: return "null"
        return str(self.val) + " -> " + self.next.__str__()

class Solution:     # Solution 1: T: O(n)   M: O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        cur = head
        while cur:
            if cur in s:
                return cur
            else:
                s.add(cur)
            cur = cur.next
        return None

class Solution_v2:      # Solution 2: T: O(n)   M: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        if not fast.next or not fast.next.next: return

        slow2 = head
        while slow.next:
            if slow == slow2: return slow
            slow, slow2 = slow.next, slow2.next
        return


def main():
    sol = Solution()
    sol = Solution_v2()

    n0, n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0), ListNode(4)
    n0.next, n1.next, n2.next, n3.next = n1, n2, n3, n1
    print(sol.detectCycle(n0).val)


main()
