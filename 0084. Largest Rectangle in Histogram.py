''' 0084. Largest Rectangle in Histogram

Hard    13K     185     Companies

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.


Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 

Constraints:        1 <= heights.length <= 10^5
                    0 <= heights[i] <= 10^4
Accepted:           621.4K
Submissions:        1.5M
Acceptance Rate:    42.3%
'''

from typing import List

class Solution():
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans, n = [], 0, len(heights)
        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][1] >= height:
                index, pre_height = stack.pop()
                ans = max(ans, pre_height * (i - index))
            stack.append((index, height))
        while stack:
            index, height = stack.pop()
            ans = max(ans, height * (n - index))
        return ans


def main():
    sol = Solution()

    heights = [2,1,5,6,2,3]     # Output: 10
    print(sol.largestRectangleArea(heights))

    heights = [2,4]             # Output: 4
    print(sol.largestRectangleArea(heights))

if __name__ == "__main__":
    main()
