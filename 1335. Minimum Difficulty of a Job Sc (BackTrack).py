''' 1335. Minimum Difficulty of a Job Schedule
Hard    1602    178     Add to List     Share
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job
schedule is the sum of difficulties of each day of the d days. The difficulty
of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty
of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule
for the jobs return -1.


Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you
cannot find a schedule for the given jobs.

Example 3:
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
 

Constraints:    1 <= jobDifficulty.length <= 300
                0 <= jobDifficulty[i] <= 1000
                1 <= d <= 10
Accepted:       84,410
Submissions:    149,988
'''

class Solution:
    # def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    def minDifficulty(self, jobDifficulty, d: int) -> int:
        def backtrack(arr, start, k):
            if len(arr[start:]) < k:
                return -1
            elif len(arr[start:]) == k:
                return sum(arr[start:])
            elif k == 1:
                return max(arr[start:])

            minCost = float('inf')
            for j in range(start, len(arr) - (k - 1)):
                curCost = max(arr[start:j + 1]) + backtrack(arr, j + 1, k - 1)
                minCost = min(minCost, curCost)

            return minCost
        return backtrack(jobDifficulty, 0, d)



def main():
    sol = Solution()
    jobDifficulty, d = [6,5,4,3,2,1], 2    # Output: 7
    print(sol.minDifficulty(jobDifficulty, d))

    jobDifficulty, d = [7, 1, 7, 1, 7 ,1], 3    # Output: 15
    print(sol.minDifficulty(jobDifficulty, d))

    jobDifficulty, d = [11,111,22,222,33,333,44,444], 6    # Output: 843
    print(sol.minDifficulty(jobDifficulty, d))


main()



'''
            11,     111,    22,     222,    33,     333,    44,     444
    
    1       11      111     111     222     222     333     333     444
    2               122     122     233     
    3
    4
    5
    6  

'''