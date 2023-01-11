''' 147. Insertion Sort List

Medium      2.4K    823     Companies

Given the head of a singly linked list, sort the list using insertion sort,
and return the sorted list's head.

The steps of the insertion sort algorithm:

 * Insertion sort iterates, consuming one input element each repetition
   and growing a sorted output list.
 * At each iteration, insertion sort removes one element from the input data,
   finds the location it belongs within the sorted list and inserts it there.
 * It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm.
The partially sorted list (black) initially contains only the first element
in the list. One element (red) is removed from the input data and inserted
in-place into the sorted list with each iteration.

    ### [D]-> 4 -> 2 -> 1 -> 3 -> None
    ###            |
    ### [D]-> 4 --{2}--> 1 -> 3 -> None

    ### [D]-> [2]-> 4 ------> 1 -> 3 -> None


Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:        The number of nodes in the list is in the range [1, 5000].
                    -5000 <= Node.val <= 5000
Accepted:           310.2K
Submissions:        614.6K
Acceptance Rate:    50.5%

'''
import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + " -> " + self.next.__str__()
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head

        def insertNode(aHead: ListNode, node: ListNode) -> None:
            curr = aHead
            while curr.next.val <= node.val: curr = curr.next
            node.next = curr.next
            curr.next = node

        # preHead = tail = ListNode(-5001)
        preHead = tail = ListNode(-math.inf)        
        preHead.next = head

        while True:
            curr = tail
            while curr.next and curr.next.val >= curr.val:
                curr = curr.next
            if not curr.next: return preHead.next
            else:
                tempNode = ListNode(curr.next.val)
                # print("# 1 ---", tempNode.val)
                tail, curr.next = curr, curr.next.next
                # print("# 2 ---", curr, "; ", curr.next)
                # print("# 3.1 -", dume, ";", tempNode, end="\n")
                insertNode(preHead, tempNode)
                # print("# 3.2 -", dume, end="\n\n")

class Solution_v2:  ### LeetCode ID: nitanshritulon
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def add(node: ListNode) -> None:
            curr = self.ans
            while(curr):
                if(curr.val < node.val):
                    prev = curr
                    curr = curr.next
                else: break
            node.next, prev.next = prev.next, node

        self.ans = ListNode(-5001)
        while(head):
            # print("# 1 ---", head)
            temp, head = head, head.next
            # print("# 2 ---", temp, "; ", head)
            temp.next = None
            # print("# 3 ---", temp)
            add(temp)
            # print("# 4 ---", self.ans, end="\n\n")
        return self.ans.next

class Solution_v3:  ### O(n * log n) solution   M: O(n)
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        # print(arr)
        newhead = curr = ListNode(-1)
        for a in sorted(arr):
            curr.next = ListNode(a)
            curr = curr.next
        return newhead.next

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()


    ### Input: head = [4,2,1,3]     Output: [1,2,3,4]
    n1, n2, n3, n4 = ListNode(4), ListNode(2), ListNode(1), ListNode(3)
    n1.next, n2.next, n3.next = n2, n3, n4
    print("Before sorted:", n1)       ### Input:  4 -> 2 -> 1 -> 3 -> None
    print(sol.insertionSortList(n1))

    ### head = [-1,5,3,4,0]     Output: [-1,0,3,4,5]
    m1, m2, m3, m4, m5 = ListNode(-1), ListNode(5), ListNode(3), ListNode(4), ListNode(0)
    m1.next, m2.next, m3.next, m4.next = m2, m3, m4, m5
    print("Before sorted:", m1)       ### Input:  -1 -> 5 -> 3 -> 4 -> 0 -> None
    print(sol.insertionSortList(m1))


if __name__ == "__main__":
    main()
