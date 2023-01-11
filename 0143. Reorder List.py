''' 143. Reorder List
Medium      7376       258      Add to List     Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → L(n-1) → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → L(n-1) → L2 → L(n-2) → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
Accepted:       581,551
Submissions:    1,144,591
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

class Solution:     # O(n^2)
    # def reorderList(self, head: Optional[ListNode]) -> None:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        
        ## get the tail
        def getTail(node):
            if not node: return None
            if not node.next: return node
            cur = node
            tail = cur.next
            while tail and tail.next:
                cur, tail = cur.next, tail.next

            cur.next = None
            return tail

        ## Traversal to list and insert the tail
        point = head
        while point and point.next and point.next.next:
            newNode = getTail(point.next)
            if not newNode: break
            temp = point.next
            point.next = newNode
            point = newNode.next = temp
        return
            
class Solution_v2:  # O(n)
    def reorderList(self, head) -> None:
        if not head or not head.next or not head.next.next: return

        # 1 Find the mid of the list
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # 2 Reverse the 2nd half of the list
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None

        # 3 merge the 1st and 2nd half and done.
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
        return


def main():

    sol = Solution_v2()
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next = n2, n3, n4
    sol.reorderList(n1)
    print(n1.toString())

    n11, n12, n13, n14, n15, n16 = ListNode(11), ListNode(12), ListNode(13), ListNode(14), ListNode(15), ListNode(16)
    n11.next, n12.next, n13.next, n14.next, n15.next = n12, n13, n14, n15, n16
    sol.reorderList(n11)
    print(n11.toString())

main()
