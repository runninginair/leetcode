'''
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times
[[s1,e1], [s2,e2], ...](si< ei), find the minimum number of conference rooms
required.

Example 1:
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2

Example 2:
Input: [[7,10], [2,4]]
Output: 1
'''

from operator import itemgetter
import heapq as hp

class Solution:
    def findMinimumRooms(self, intervals)->int:
        if not intervals:
            return 0
        n = len(intervals)
        if n < 2:
            return n

        schedule = sorted(intervals, key=itemgetter(0))
        end = []
        hp.heappush(end, schedule.pop(0)[1])

        res = 1

        for meet in schedule:
            if meet[0] >= end[0]:
                hp.heappop(end)
            hp.heappush(end, meet[1])
            # hp.heapify(end)
            res = max(res, len(end))

        return res



def main():
    sol = Solution()
    Input = [[0,30],[5,10],[15,20]]     # Output: 2
    print(sol.findMinimumRooms(Input))

    Input = [[7,10],[2,4]]              # Output: 1
    print(sol.findMinimumRooms(Input))

    Input = [[7,10],[4,6], [2,4], [6,7]]   # Output: 1
    print(sol.findMinimumRooms(Input))

    Input = None   # Output: 0
    print(sol.findMinimumRooms(Input))

    Input = []   # Output: 0
    print(sol.findMinimumRooms(Input))

    Input = [[7,10]]   # Output: 1
    print(sol.findMinimumRooms(Input))

    Input = [[14,24], [12,18], [12,14], [16,22], [5,16],[2,12],[14,20]]   # Output: 4
    print(sol.findMinimumRooms(Input))


main()
