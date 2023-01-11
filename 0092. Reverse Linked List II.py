''' 92. Reverse Linked List II
Medium  8092    356     Add to List     Share
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:    The number of nodes in the list is n.
                1 <= n <= 500
                -500 <= Node.val <= 500
                1 <= left <= right <= n
 
Follow up: Could you do it in one pass?
Accepted:       579,960
Submissions:    1,278,867

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        res = ""
        while self:
            res += (str(self.val) + " -> ")
            self = self.next
        res += 'None'
        return res

class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    def reverseBetween(self, head, left: int, right: int):
        if not head.next or left == right: return head
        
        curr, index = head, 1
        #1 Find the left node.
        while curr.next and index != left-1:
            curr = curr.next
            index += 1
            
        temp, prev, nextt = None, None, curr.next
        tail = curr.next
        print("tail.val =", tail.val)
        curr.next = None
        
        while nextt and index != right:
            temp = nextt.next
            nextt.next = prev
            prev = nextt
            nextt = temp
            index += 1
        print("temp.val =",temp.val)
            
        curr.next = prev
        if tail: tail.next = temp
        return head


def main():

    sol = Solution()
    n1, n2, n3, n4, n5, n6, n7 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6), ListNode(7)
    n1.next, n2.next, n3.next, n4.next, n5.next, n6.next = n2, n3, n4, n5, n6, n7

    print(n1.toString())
    n0 = sol.reverseBetween(n1, 4, 6)
    print(n0.toString())

main()