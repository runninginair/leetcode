''' 206. Reverse Linked List
Easy       15237        255     Add to List     Share
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:    The number of nodes in the list is the range [0, 5000].
                -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted:       2,638,816
Submissions:    3,646,789
'''

class LinkedList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if not self: return "null"
        res, cur = "", self
        while cur:
            res += str(cur.val) + " -> "
            cur = cur.next
        return res + "null"

class Solution:        ### Iteratively Time: O(n), Space: O(1)
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            # temp = curr.next
            # curr.next = prev
            # prev = curr
            # curr = temp
        return prev

class Solution_v2:        ### Recursively Time: O(n), Space: O(n)
    def reverseList(self, head):
        if not head:
            return None
        new_head = head

        if head.next:
            print("Head.next =", head.next.val, "\t", head.next)
            new_head = self.reverseList(head.next)
            print("New Head", new_head, "\nOLD head", head, "\n")
            head.next.next = head

        head.next = None
        return new_head

class Solution_v3:      ### Recursively Time: O(n), Space: O(n)
    def flipMapping(self, cur, nxt):
        if nxt.next: self.flipMapping(cur.next, nxt.next)
        else: self.new_head = nxt
        nxt.next = cur

    def reverseList(self, head):
        if not head or not head.next: return head
        self.new_head = None
        self.flipMapping(head, head.next)
        head.next = None
        return self.new_head

def main():
    sol = Solution()        ### Iteration
    sol = Solution_v2()     ### Recursion
    sol = Solution_v3()     ### Recursion with helper

    # n1, n2, n3, n4, n5, n6 = LinkedList(1), LinkedList(2), LinkedList(3), LinkedList(4), LinkedList(5), LinkedList(6)
    # n1.next, n2.next, n3.next, n4.next, n5.next = n2, n3, n4, n5, n6

    n1, n2, n3 = LinkedList(1), LinkedList(2), LinkedList(3)
    n1.next, n2.next,  = n2, n3
    print(n1)
    print(sol.reverseList(n1))

main()
