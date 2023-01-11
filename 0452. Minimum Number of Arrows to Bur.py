''' 452. Minimum Number of Arrows to Burst Balloons

Medium      4K      116      Companies

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where 
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from
different points along the x-axis. A balloon with xstart and xend is burst by
an arrow shot at x if xstart <= x <= xend. There is no limit to the number of
arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting
any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot
to burst all balloons.


Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:        1 <= points.length <= 10^5
                    points[i].length == 2
                    -2^31 <= xstart < xend <= 2^31 - 1
Accepted:           216.4K
Submissions:        405.7K
Acceptance Rate:    53.3%
'''

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans, i, N = 0, 0, len(points)

        while i < N:
            ans += 1
            next = i + 1
            while next < N and points[next][0] <= points[i][1]: next += 1
            i = next

        return ans

class Solution_v2:  ### Moving from left to right, sort the points based on end point.
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res, curEnd = 1, points[0][1]
        for start,end in points:
            if start>curEnd:
                curEnd = end
                res += 1
        return res

class Solution_v3: ### Moving from right to left, sort the points based on start point.
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res, curStart = 1, points[-1][0]
        for start,end in reversed(points):
            if end<curStart:
                curStart = start
                res += 1
        return res

class Solution_v4:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        points.sort(key = lambda x: x[1])      # Example:  points = [[2,4],[1,6],[1,3],[7,8]]
                                               #      points.sort = [[1,3],[2,4],[1,6],[7,8]]
        tally, bow = 1, points[0][1]
                                               #                     ––––––– [7,9]
        for start, end in points:              #   ––––––––––––––––          [1,6] 
            if bow < start:                    #      –––––––                [2,4]
                bow = end                      #   –––––––                   [1,3]
                tally += 1                     #   1  2  3  4  5  6  7  8  9
                                               #         |                 |     
        return tally                           #     tally = 1         tally = 2

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    points = [[10,16],[2,8],[1,6],[7,12]]   # Output: 2
    print(sol.findMinArrowShots(points))

    points = [[1,2],[3,4],[5,6],[7,8]]      # Output: 4
    print(sol.findMinArrowShots(points))

    points = [[1,2],[2,3],[3,4],[4,5]]      # Output: 2
    print(sol.findMinArrowShots(points))


if __name__ == "__main__":
    main()

