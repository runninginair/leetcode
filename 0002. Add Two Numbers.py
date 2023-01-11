''' 2. Add Two Numbers

Medium      23.4K      4.5K      Companies

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:      2 -> 4 -> 3
            +   5 -> 6 -> 4     
            =>  7 -> 0 -> 8

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:    The number of nodes in each linked list is in the range [1, 100].
                0 <= Node.val <= 9
                It is guaranteed that the list represents a number that does not have leading zeros.
Accepted:           3.3M
Submissions:        8.3M
Acceptance Rate:    40.0%
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return str(self.val) + " -> " + self.next.__str__()


class Solution:     ### T: O(l1 + l2)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(node:  Optional[ListNode]) -> int:
            res = n = 0
            while node:
                res += node.val * 10 ** n
                n += 1
                node = node.next
            return res
        def generateList(num: int) -> Optional[ListNode]: 
            if num == 0: return ListNode(0)
            dummy = curr = ListNode(-1)
            while num > 0:
                digit = num - num // 10 * 10
                curr.next = ListNode(digit)
                curr = curr.next
                num //= 10
            return dummy.next
        return generateList(getNum(l1) + getNum(l2))

class Solution_v1:     ### T: O(l1 + l2)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
        return dummy.next


def main():
    sol = Solution()
    sol = Solution_v1()

    n1, n2, n3, n11, n12, n13 = ListNode(2), ListNode(4), ListNode(3), ListNode(5), ListNode(6), ListNode(4)
    n1.next, n2.next, n11.next, n12.next = n2, n3, n12, n13
    # print(n1)       # 2 -> 4 -> 3 -> None
    # print(n11)      # 5 -> 6 -> 4 -> None
    print(sol.addTwoNumbers(n1, n11))       # Output: 7 -> 0 -> 8 -> None

    u1, u11 = ListNode(0), ListNode(0)
    # print(u1)       # 0 -> None
    # print(u11)      # 0 -> None
    print(sol.addTwoNumbers(u1, u11))       # Output: 0 -> None

    v1, v2, v3, v4, v5, v6, v7, v11, v12, v13, v14 = ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9)
    v1.next, v2.next, v3.next, v4.next, v5.next, v6.next, v11.next, v12.next, v13.next =  v2, v3, v4, v5, v6, v7, v12, v13, v14
    # print(v1)       # 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> None
    # print(v11)      # 9 -> 9 -> 9 -> 9 -> None
    print(sol.addTwoNumbers(v1, v11))       # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None


main()
