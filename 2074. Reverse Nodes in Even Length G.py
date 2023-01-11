''' 2074. Reverse Nodes in Even Length Groups
Medium      344     252     Add to List     Share

You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose
lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length
of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

 

Example 1:
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.

Example 2:
Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.

Example 3:
Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
 

Constraints:    The number of nodes in the list is in the range [1, 10^5].
                0 <= Node.val <= 10^5
Accepted:       13,184
Submissions:    25,566
'''

# Definition for singly-linked list.
from re import L


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self,head) -> str:
        if not head: return 'None'
        return str(head.val) + " -> " + self.toString(head.next)

### https://leetcode.com/problems/reverse-nodes-in-even-length-groups/discuss/1577032/Python-Reverse-Linked-List-O(1)-Space
class Solution:
    # def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseEvenLengthGroups(self, head):

        prev = head
        d = 2 # the head doesn't need to be reversed anytime so starts with length 2
        while prev.next:
            node, n = prev, 0
            print(" # 0     node.val =", node.val, "  d =", d)
            for _ in range(d):
                if not node.next:
                    break
                n += 1
                node = node.next
            print(" # 1     node.val =", node.val, "  n =", n)
            if n & 1:  # odd length
                prev = node
                print(" # 2      prev = node =",prev.val)
            else:      # even length
                node, rev = prev.next, None
                print(" # 3      node =", node.val)
                for _ in range(n):
                    print(rev.val if rev else None, node.next.val if node.next else None, node.val if node else None)
                    node.next, node, rev = rev, node.next, node
                # print(rev.val if rev else None, node.next.val if node.next else None, node.val if node else None)
                prev.next.next, prev.next, prev = node, rev, prev.next
            d += 1
            print("######\n")
        return head

def main():
    sol = Solution()
    ### Input: head = [5,2,6,3,9,1,7,3,8,4] Output: [5,6,2,3,9,1,4,8,3,7]
    # n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = ListNode(5), ListNode(2), ListNode(6), ListNode(3), ListNode(9), ListNode(1), ListNode(7), ListNode(3), ListNode(8), ListNode(4)
    # n1.next,n2.next,n3.next,n4.next,n5.next,n6.next,n7.next,n8.next,n9.next = n2,n3,n4,n5,n6,n7,n8,n9,n10
    # print(n1.toString(n1))
    # new_head = sol.reverseEvenLengthGroups(n1)
    # print(n1.toString(new_head))

    # ### Input: head = [5,2,6,3,9,1,7,3,8,4,11,12] Output: [5,6,2,3,9,1,4,8,3,7,12,11]
    # n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12 = ListNode(5), ListNode(2), ListNode(6), ListNode(3), ListNode(9), ListNode(1), ListNode(7), ListNode(3), ListNode(8), ListNode(4), ListNode(11), ListNode(12)
    # n1.next,n2.next,n3.next,n4.next,n5.next,n6.next,n7.next,n8.next,n9.next,n10.next,n11.next = n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12
    # print(n1.toString(n1))
    # new_head = sol.reverseEvenLengthGroups(n1)
    # print(n1.toString(new_head))

    n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = ListNode(0), ListNode(2), ListNode(3), ListNode(0), ListNode(0), ListNode(0), ListNode(7), ListNode(8), ListNode(9), ListNode(10)
    n1.next,n2.next,n3.next,n4.next,n5.next,n6.next,n7.next,n8.next,n9.next = n2,n3,n4,n5,n6,n7,n8,n9,n10
    print(n1.toString(n1))
    new_head = sol.reverseEvenLengthGroups(n1)
    print(n1.toString(new_head))


main()
