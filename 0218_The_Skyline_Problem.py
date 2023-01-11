''' 218. The Skyline Problem
Hard      4529      226     Add to List     Share
A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Given the locations and
heights of all the buildings, return the skyline formed by these buildings
collectively.

The geometric information of each building is given in the array buildings
where buildings[i] = [left_i, right_i, height_i]:

    * left_i is the x coordinate of the left edge of the ith building.
    * right_i is the x coordinate of the right edge of the ith building.
    * height_i is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely
flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their
x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
endpoint of some horizontal segment in the skyline except the last point in the
list, which always has a y-coordinate 0 and is used to mark the skyline's
termination where the rightmost building ends. Any ground between the leftmost
and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the
output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not
acceptable; the three lines of height 5 should be merged into one in the final
output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure
B represent the key points in the output list.

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:    1 <= buildings.length <= 104
                0 <= lefti < righti <= 231 - 1
                1 <= heighti <= 231 - 1

buildings is sorted by lefti in non-decreasing order.
Accepted:       229,218
Submissions:    571,365
'''

import heapq

class Solution:
    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    def getSkyline(self, buildings):
        events, res, pre_highest, highest = [], [], [0], 0
        for l, r, h in buildings:
            events.append((l, h, 0))
            events.append((r, h, 1))
        
        events.sort(key= lambda x:(x[0], -1*(x[1]) if x[2]==0 else x[1]))
        # print(events, end="\n\n")

        for i, e in enumerate(events):
            if e[2] == 0:
                pre_highest.append(e[1])
                if e[1] == highest: continue
                heapq._heapify_max(pre_highest)
                # print(pre_highest)
                if e[1] == pre_highest[0]: 
                    highest = e[1]
                    res.append([e[0], e[1]])
            else:   # if e[2] == 1:
                for i in range(len(pre_highest)-1, -1, -1):
                    if pre_highest[i] == e[1]:
                        pre_highest.pop(i)
                        break
                heapq._heapify_max(pre_highest)
                if highest != pre_highest[0]:
                    if e[0] == res[-1][0] and e[1] < res[-1][1]:
                        res[-1][1] = e[1]
                        highest = pre_highest[0]
                    else:
                        res.append([e[0], pre_highest[0]])
                        highest = pre_highest[0]

        return res

def main():
    sol = Solution()
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(sol.getSkyline(buildings))
    # Expected: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    
    buildings = [[0,2,3],[2,5,3]]       # Expected: [[0,3],[5,0]]
    print(sol.getSkyline(buildings))

    buildings = [[1,2,1],[1,2,2],[1,2,3]]    # Expected: [[1,3],[2,0]]
    print(sol.getSkyline(buildings))

main()
