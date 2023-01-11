''' 725. Split Linked List in Parts
Medium       2119       210     Add to List     Share

Given the head of a singly linked list and an integer k, split the linked list
into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should
have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.


Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
 

Constraints:    The number of nodes in the list is in the range [0, 1000].
                0 <= Node.val <= 1000
                1 <= k <= 50
Accepted:       104,899
Submissions:    183,297
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toString(self, node) -> str:
        if not node: return 'None'
        else: return str(node.val) + ' -> ' + self.toString(node.next)
        
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: return None
        if not head.next:
            return head.append([None for _ in range(k - 1)])

        # Count the number of ListNode as counter (total).
        counter, curr, res = 1, head, []
        while curr.next:
            counter += 1
            curr = curr.next
        curr, total = head, counter
            
        if k >= counter:
            while counter > 0:
                new_node = curr
                new_node.next = None
                res.append(new_node)
                counter -= 1
            for i in range(k - counter):
                res.append([])
            return res
        
        counter = total
        len_arr = [0 for _ in range(k)]
        for i in range(counter):
            len_arr[i % k] += 1
        print(len_arr)


        return res
        

def main():
    sol = Solution()
    # Input: head = [1,2,3,4,5], k = 2    Output: [4,5,1,2,3]    
    n1, n2,n3,n4,n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next,n2.next,n3.next,n4.next = n2, n3, n4, n5
    print(n1.toString(n1))
    res = sol.splitListToParts(n1, 7)
    for r in res:
        print(r.toString(r))
    # print(res.toString(res))

main()
