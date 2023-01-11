'''
0042

42. Trapping Rain Water
Hard    22011   295     Add to List     Share
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
Accepted:       1,291,455
Submissions:    2,226,647
'''


from turtle import right


class Solution0:  # Failed Due to: leetCode Time Limit Exceeded
    # def trap(self, height: List[int]) -> int:
    def trap(self, height) -> int:
        res, n = 0, len(height)
        if n <= 2: return 0
        
        def findMaxHeight(height, start, end):
            max_h = max_i = 0
            for i in range(start, end + 1):
                if height[i] > max_h: 
                    max_h, max_i = height[i], i
            return max_h, max_i
        
        _, key = findMaxHeight(height, 0, n - 1)
        # print("MID: ", _, key)

        def getVol(height, bar, l, r):
            vol = 0
            for i in range(l, r + 1):
                # print("height[i] =", height[i])
                vol += bar - height[i]
            return vol

        # Caculate left side trap
        left_max, left_end = findMaxHeight(height, 0, key - 1)
        res += getVol(height, left_max, left_end, key - 1)
        # print("left_max, left_end, res =",left_max, left_end, res)
        # print()
        while left_end > 1 and left_max > 0:
            bar = left_end
            left_max, left_end = findMaxHeight(height, 0, bar - 1)
            res += getVol(height, left_max, left_end, bar - 1)
            # print("While --> left_max, left_end, res =",left_max, left_end, res)

        # Caculate right side trap
        right_max, right_end = findMaxHeight(height, key + 1, n - 1)
        res += getVol(height, right_max, key + 1, right_end)
        while right_end < n - 1 and right_max > 0:
            bar = right_end
            right_max, right_end = findMaxHeight(height, bar + 1, n - 1)
            res += getVol(height, right_max, bar + 1, right_end)

        return res        

class Solution1:    # Time Complexity: O(n) Solution    Space complexity: O(n)
    def trap(self, height) -> int:
        res, n = 0, len(height)
        if n <= 2: return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftHeight = height[0]
        rightHeight = height[n-1]

        for i in range(1, n - 1):
            if height[i - 1] > leftHeight:
                leftMax[i] = height[i - 1]
                leftHeight = height[i - 1]
            else:
                leftMax[i] = leftHeight

        for i in range(n - 2, 0, -1):
            if height[i + 1] > rightHeight:
                rightMax[i] = height[i + 1]
                rightHeight = height[i + 1]
            else:
                rightMax[i] = rightHeight

        # print(leftMax)
        # print(rightMax)

        for i in range(1, n - 1):
            bar = min(leftMax[i], rightMax[i])
            if height[i] < bar:
                res += (bar - height[i])

        return res

def main():
    sol = Solution1()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # Output: 6
    print(sol.trap(height))

    height = [4,2,0,3,2,5]  # Output: 9
    print(sol.trap(height))

    height = [3,0,5,3,3,6,5,0,3,6]  # Output: 17
    print(sol.trap(height))    


if __name__ == '__main__':
    main()
