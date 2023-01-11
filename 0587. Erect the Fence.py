''' 587. Erect the Fence
Hard    638     389     Add to List     Share

You are given an array trees where trees[i] = [xi, yi] represents the location
of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it
is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.


Example 1:
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:
Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
 
Constraints:        1 <= points.length <= 3000
                    points[i].length == 2
                    0 <= xi, yi <= 100
                    All the given points are unique.
Accepted:       26,190
Submissions:    60,115
'''

from typing import List


class Solution:     ###  Convex Hull | Graham's Scan Algorithm   
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare_slopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        lower, upper = [], []

        for point in sorted(trees):
            # print(trees, "\tPoint:", point, "\tLOWER:", lower, "\tUPPER:",upper)
            while len(lower) > 1 and compare_slopes(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) > 1 and compare_slopes(upper[-2], upper[-1], point) > 0:
                upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))
        return list(set(lower + upper))

def main():
    sol = Solution()
    # points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    # print(sol.outerTrees(points))   # Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

    # points = [[1,2],[2,2],[4,2]]
    # print(sol.outerTrees(points))   # Output: [[4,2],[2,2],[1,2]]

    points = [[1,1],[2,3],[3,2],[2,2]]
    print(sol.outerTrees(points))   # Output: [[1,1],[3,2],[2,3]]

main()
