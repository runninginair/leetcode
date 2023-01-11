''' 61. Rotate List
Medium      6634      1317      Add to List     Share
Given the head of a linked list, rotate the list to the right by k places.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:    The number of nodes in the list is in the range [0, 500].
                -100 <= Node.val <= 100
                0 <= k <= 2 * 10 ^ 9
Accepted:       649,934
Submissions:    1,818,341
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toString(self, node) -> str:
        if not node: return 'None'
        else: return str(node.val) + ' -> ' + self.toString(node.next)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k == 0 or not head.next: return head

        # Caculate the length of the list
        counter, curr = 1, head
        while curr.next:
            counter += 1
            curr = curr.next
        tail_node = curr

        k = k % counter
        if k == 0: return head
        cut = counter - k

        rem = curr = head
        while cut > 1:
            curr = curr.next
            cut -= 1

        new_head = curr.next

        curr.next = None
        tail_node.next = rem

        return new_head

def main():
    sol = Solution()
    # Input: head = [1,2,3,4,5], k = 2    Output: [4,5,1,2,3]    
    n1, n2,n3,n4,n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next,n2.next,n3.next,n4.next = n2, n3, n4, n5
    print(n1.toString(n1))
    res = sol.rotateRight(n1, 2)
    print(res.toString(res))

main()
