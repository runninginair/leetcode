''' 502. IPO

Hard    1.1K    95     Companies

Suppose LeetCode will start its IPO soon. In order to sell a good price of its
shares to Venture Capital, LeetCode would like to work on some projects to
increase its capital before the IPO. Since it has limited resources, it can
only finish at most k distinct projects before the IPO. Help LeetCode design
the best way to maximize its total capital after finishing at most k distinct
projects.

You are given n projects where the i-th project has a pure profit profits[i]
and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its
pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your
final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.


Example 1:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation:
Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2
to get the maximum capital. Therefore, output the final maximized capital,
which is 0 + 1 + 3 = 4.

Example 2:
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:        1 <= k <= 10^5
                    0 <= w <= 10^9
                    n == profits.length
                    n == capital.length
                    1 <= n <= 10^5
                    0 <= profits[i] <= 10^4
                    0 <= capital[i] <= 10^9
Accepted:           41.7K
Submissions:        92.2K
Acceptance Rate:    45.2%
'''

from typing import List
import heapq

class Solution:     ### My Greedy Solution      T: O(n * log(n))    M: O(n)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        N, otherProjects, firstQueue = len(profits), [], []
        for i in range(N):
            if capital[i] <= w: firstQueue.append(-profits[i])
            else: otherProjects.append([capital[i], profits[i]])
        heapq.heapify(firstQueue)
        heapq.heapify(otherProjects)
        
        while k > 0 and firstQueue:
            w -= heapq.heappop(firstQueue)
            k -= 1
            while otherProjects and otherProjects[0][0] <= w:
                heapq.heappush(firstQueue, -heapq.heappop(otherProjects)[1])
        return w


class Solution_official:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        # heapq is a min heap, but we need a max heap
        # so we will store negated elements
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element
                heapq.heappush(q, -projects[ptr][1])
                ptr += 1
            if not q: break
            # pop a negated element
            w += -heapq.heappop(q)
        return w


def main():
    sol = Solution()

    k, w, profits, capital = 2, 0, [1,2,3], [0,1,1]
    print(sol.findMaximizedCapital(k, w, profits, capital)) # Expect Output: 4

    k, w, profits, capital = 3, 0, [1,2,3], [0,1,2]
    print(sol.findMaximizedCapital(k, w, profits, capital)) # Expect Output: 6

if __name__ == "__main__":
    main()
