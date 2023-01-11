''' 149. Max Points on a Line

Hard    3.2K    388     Companies

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane, return the maximum number of points that lie on the same straight line.


Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 
Constraints:        1 <= points.length <= 300
                    points[i].length == 2
                    -104 <= xi, yi <= 104
                    All the points are unique.
Accepted:           316.6K
Submissions:        1.3M
Acceptance Rate:    24.5%
'''

from typing import List

class Solution:     ### Brute Force Solution    T: O(n^3)   M: O(1)
    def maxPoints(self, points: List[List[int]]) -> int:
        n, ans = len(points), 2
        if n < 3: return n
        def isOneLine(x: List[int], y: List[int], z: List[int]) -> bool:
            return (x[0] - y[0]) * (y[1] - z[1]) == (y[0] - z[0]) * (x[1] - y[1])
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                cur = 2
                for k in range(j + 1, n):
                    if isOneLine(points[i], points[j], points[k]): 
                        cur += 1
                        ans = max(ans, cur)
        return ans

import collections, math

### LeetCode Official Solution:
class Solution_v2:      ### math.atan2 Solution    T: O(n^2)   M: O(n^2)
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result


def main():
    sol = Solution()
    sol = Solution_v2()

    # points = [[1,1],[2,2],[3,3]]    # Output: 3
    # print(sol.maxPoints(points))

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]      # Output: 4
    print(sol.maxPoints(points))

    # points = [[0,0],[1,-1],[1,1]]   # Output: 2
    # print(sol.maxPoints(points))

if __name__ == "__main__":
    main()
