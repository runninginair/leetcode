''' 82. Remove Duplicates from Sorted List II
Medium  6713    185 Add to List     Share
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the
linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:    The number of nodes in the list is in the range [0, 300].
                -100 <= Node.val <= 100
                The list is guaranteed to be sorted in ascending order.
Accepted:       546,311
Submissions:    1,204,483
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printOut(self):
        while self:
            print(self.val, end=" -> ")
            self = self.next
        print("None")

class Solution:
    def deleteDuplicates(self, head:ListNode):
        if not head: return None
        if not head.next: return head
        
        dic = {}
        rem = cur = head
        while cur:
            if cur.val in dic:
                dic[cur.val] += 1
            else:
                dic[cur.val] = 1
            cur = cur.next
        # print(dic)

        while rem and dic[rem.val] > 1:
            rem = rem.next
        if not rem:
            return None
        # rem.printOut()

        newHead = rem
        # newHead.printOut()
        # print(dic)
        while rem and rem.next:
            while rem.next and dic[rem.next.val] > 1:
                rem.next = rem.next.next
            rem = rem.next
        return newHead

def main():
    sol = Solution()
    n1, n2, n3, n4, n5, n6, n7 = ListNode(1), ListNode(2), ListNode(3), ListNode(3), ListNode(4), ListNode(4), ListNode(5)
    n1.next, n2.next, n3.next, n4.next, n5.next, n6.next = n2, n3, n4, n5, n6, n7
    n1.printOut()
    n0 = sol.deleteDuplicates(n1)
    n0.printOut()

    n11, n12, n13, n14, n15, = ListNode(1), ListNode(1), ListNode(1), ListNode(2), ListNode(3)
    n11.next, n12.next, n13.next, n14.next = n12, n13, n14, n15
    n11.printOut()
    n10 = sol.deleteDuplicates(n11)
    n10.printOut()


main()
