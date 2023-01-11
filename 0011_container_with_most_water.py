'''
11. Container With Most Water
Medium  20221   1070    Add to List     Share
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
Accepted:       1,755,784
Submissions:    3,236,645

'''

class Solution:         # Time: O(n^2)
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height) -> int:
        n = len(height)
        max = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if height[j] < height[j - 1]: continue
                temp = (min(height[i], height[j])) * (j - i)
                if temp > max: max = temp
        return max

class Solution_v2:      # Time: O(n)
    def maxArea(self, height) -> int:
        n = len(height)
        p1, p2 = 0, n - 1
        max = min(height[p1], height[p2]) * (p2 - p1)
        while(p1 < p2):
            if (height[p1] < height[p2]):
                p1 += 1
            else:
                p2 -= 1
            temp = min(height[p1], height[p2]) * (p2 - p1)
            if temp > max:
                max = temp
        return max


def main():
    sol = Solution_v2()
    h = [1,8,6,2,5,4,8,3,7]     # Output: 49
    print(sol.maxArea(h))

main()
