''' 57. Insert Interval

Medium      6.6K    472     Companies

You are given an array of non-overlapping intervals intervals where
intervals[i] = [start-i, end-i] represent the start and the end of the i-th
interval and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:        0 <= intervals.length <= 10^4
                    intervals[i].length == 2
                    0 <= starti <= endi <= 10^5
                    intervals is sorted by starti in ascending order.
                    newInterval.length == 2
                    0 <= start <= end <= 10^5
Accepted:           659.9K
Submissions:        1.7M
Acceptance Rate:    38.1%
'''

from typing import List

class Solution:     ### Sort & Merge Solution   T: O(n * log n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals.pop(0)]
        for interval in intervals:
            if interval[0] > res[-1][1]: res.append(interval)
            else: res[-1][1] = max(res[-1][1], interval[1])
        return res

class Solution_v2:      ### Directly Merge Solution   T: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        elif newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        elif intervals[-1][1] < newInterval[0]: return intervals + [newInterval]
        else:
            start, end = newInterval[0], newInterval[1]
            ans = []
            merged = False
            for x, y in intervals:
                if ans and x <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], y)
                    merged = True
                elif y < start: ans.append([x, y])
                elif x > end:
                    if not merged:
                        ans.append([start, end])
                        merged = True
                    ans.append([x, y])
                elif y >= start:
                    ans.append([min(x, start), max(y, end)])
                    merged = True
        return ans

class Solution_v3:      ### Directly Merge Solution   T: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        elif newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        elif intervals[-1][1] < newInterval[0]: return intervals + [newInterval]        

        ans, isMerged = [], False
        for x, y in intervals:
            if y < newInterval[0]: ans.append([x, y])
            elif ans and x <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], y)
                isMerged = True
            elif x > newInterval[1]:
                if not isMerged:
                    ans.append(newInterval)
                    isMerged = True
                ans.append([x, y])
            elif y >= newInterval[0]:
                ans.append([min(x, newInterval[0]), max(y, newInterval[1])])
                isMerged = True
        return ans

''' ### Official Java Solution

class Solution {
    // Returns true if the intervals a and b have a common element.
    boolean doesIntervalsOverlap(int[] a, int[] b) {
        return Math.min(a[1], b[1]) - Math.max(a[0], b[0]) >= 0;
    }

    // Return the interval having all the elements of intervals a and b.
    int[] mergeIntervals(int[] a, int[] b) {
        int[] newInterval = {Math.min(a[0], b[0]), Math.max(a[1], b[1])};
        return newInterval;
    }

    // Insert the interval newInterval, into the list interval keeping the sorting order intact.
    int[][] insertInterval(int[][] intervals, int[] newInterval) {
        boolean isIntervalInserted = false;
        List<int[]> list = new ArrayList<>(Arrays.asList(intervals));

        for (int i = 0; i < intervals.length; i++) {
            if (newInterval[0] < intervals[i][0]) {
                // Found the position, insert the interval and break from the loop.
                list.add(i, newInterval);
                isIntervalInserted = true;
                break;
            }
        }

        // If there is no interval with a greater value of start value,
        // then the interval must be inserted at the end of the list.
        if (!isIntervalInserted) {
            list.add(newInterval);
        }

        return list.toArray(new int[list.size()][2]);
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        // Insert the interval first before merge processing.
        intervals = insertInterval(intervals, newInterval);

        List<int[]> answer = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            int[] currInterval = {intervals[i][0], intervals[i][1]};
            // Merge until the list gets exhausted or no overlap is found.
            while (i < intervals.length && doesIntervalsOverlap(currInterval, intervals[i])) {
                currInterval = mergeIntervals(currInterval, intervals[i]);
                i++;
            }
            // Decrement to ensure we don't skip the interval due to outer for-loop incrementing.
            i--;
            answer.add(currInterval);
        }

        return answer.toArray(new int[answer.size()][2]);
    }
}

'''
''' ### Official Java Solution to Python    NOT CORRECT!!!
class Solution_v5:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ### Returns true if the intervals a and b have a common element.
        def doesIntervalsOverlap(a: List[int], b: List[int]) -> bool:
            return min(a[1], b[1]) >= max(a[0], b[0])
        
        ### Return the interval having all the elements of intervals a and b.
        def mergeIntervals(a: List[int], b: List[int]) -> List[int]:
            newInterval = [min(a[0], b[0]), max(a[1], b[1])]
            return newInterval

        ### Insert the interval newInterval, into the list interval keeping the sorting order intact.
        def insertInterval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            isIntervalInserted = False
            # List<int[]> list = new ArrayList<>(Arrays.asList(intervals));
            for i in range(len(intervals)):
                if newInterval[0] < intervals[i][0]:
                    ### Found the position, insert the interval and break from the loop.
                    intervals.insert(i, newInterval)
                    isIntervalInserted = True
                    break

            ### If there is no interval with a greater value of start value,
            ### then the interval must be inserted at the end of the list.
            if not isIntervalInserted: intervals.append([newInterval])
            return intervals
        
        intervals = insertInterval(intervals, newInterval)
        answer = []
        for i in range(len(intervals)):
            currInterval = [intervals[i][0], intervals[i][1]]
            ### Merge until the list gets exhausted or no overlap is found.
            while (i < len(intervals) and doesIntervalsOverlap(currInterval, intervals[i])):
                currInterval = mergeIntervals(currInterval, intervals[i])
                i += 1
            ### Decrement to ensure we don't skip the interval due to outer for-loop incrementing.
            i -= 1
            answer.append(currInterval)

        return answer
'''


def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()
    # sol = Solution_v5()

    intervals, newInterval = [[1,3],[6,9]], [2,5]  # Output: [[1,5],[6,9]]
    print(sol.insert(intervals, newInterval))

    intervals,  newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]     # Output: [[1,2],[3,10],[12,16]]
    print(sol.insert(intervals, newInterval))

    intervals, newInterval = [[1,2],[6,9]], [3,5]  # Output: [[1,2],[3,5],[6,9]]
    print(sol.insert(intervals, newInterval))    

    intervals, newInterval = [[3,5],[6,9]], [1,2]  # Output: [[1,2],[3,5],[6,9]]
    print(sol.insert(intervals, newInterval))

    intervals, newInterval = [[1,3],[5,6]], [8,9]  # Output: [[1,3],[5,6],[8,9]]
    print(sol.insert(intervals, newInterval))

    intervals = [[1,5]]
    newInterval = [6,8]
    print(sol.insert(intervals, newInterval))    

    intervals = [[1,5]]
    newInterval = [0,3]
    print(sol.insert(intervals, newInterval))

    intervals = [[0,10],[14,14],[15,20]]
    newInterval = [11,11]
    print(sol.insert(intervals, newInterval))


main()
