'''
252. Meeting Rooms
Question
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true

'''

from operator import itemgetter


class Solution:
    def canAttendMeetings(self, intervals) ->bool:
        if not intervals: return True
        n = len(intervals)
        if n < 2: return True
        sche = sorted(intervals, key=itemgetter(0))
        # print(sche)
        for i in range(1, len(sche)):
            if sche[i][0] < sche[i-1][1]:
                return False
        return True

def main():
    sol = Solution()
    Input = [[0,30],[5,10],[15,20]]     # Output: false
    print(sol.canAttendMeetings(Input))

    Input = [[7,10],[2,4]]              # Output: true
    print(sol.canAttendMeetings(Input))

    Input = [[7,10],[4,6], [2,4], [6,7]]   # Output: true
    print(sol.canAttendMeetings(Input))

    Input = None   # Output: true
    print(sol.canAttendMeetings(Input))

    Input = []   # Output: true
    print(sol.canAttendMeetings(Input))

    Input = [[7,10]]   # Output: true
    print(sol.canAttendMeetings(Input))


main()
