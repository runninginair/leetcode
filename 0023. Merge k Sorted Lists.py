''' 23. Merge k Sorted Lists
Hard      14701      550     Add to List     Share

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:        k == lists.length
                    0 <= k <= 10^4
                    0 <= lists[i].length <= 500
                    -10^4 <= lists[i][j] <= 10^4
                    lists[i] is sorted in ascending order.
                    The sum of lists[i].length will not exceed 10^4.
Accepted:       1,457,951
Submissions:    3,012,128

'''

from typing import List, Optional
import heapq

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def toString(self, head):
        if not head: return 'None'
        else: return str(head.val) + ' -> ' + self.toString(head.next)


class Solution_v0:  ### Brute Force     Time: O(n log(n))     Memory: O(n)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for list in lists:
            cur = list
            while cur:
                arr.append(cur.val)
                cur = cur.next
        arr.sort()
        head = None
        if arr:
            head = ListNode(arr.pop(0))
            cur = head
            while arr:
                cur.next = ListNode(arr.pop(0))
                cur = cur.next
        return head

class Solution_V1:  ### Heap | Priority Queue   Time:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        preHead = ListNode(0)
        heapq.heapify(lists, key = lambda x: x.value)

        for list in lists:
            print(list.toString(list))

        return



def main():
    # sol = Solution_v0()
    sol = Solution_V1()
    n1, n2, n3 = ListNode(1), ListNode(4), ListNode(5)
    m1, m2, m3 = ListNode(1), ListNode(3), ListNode(4)
    p1, p2 = ListNode(2), ListNode(6)
    n1.next, n2.next, m1.next, m2.next, p1.next = n2, n3, m2, m3, p2
    ls = [n1, m1, p1]
    # lists = [[1,4,5],[1,3,4],[2,6]]   # Output: [1,1,2,3,4,4,5,6]
    # print(n1.toString(n1))
    # print(m1.toString(m1))
    # print(p1.toString(p1))
    newHead = sol.mergeKLists(ls)
    print(newHead.toString(newHead))


main()