''' 2187. Minimum Time to Complete Trips

Medium      979     63      Companies

You are given an array time where time[i] denotes the time taken by the i-th bus
to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start
immediately after completing the current trip. Also, each bus operates independently;
that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses
should make in total. Return the minimum time required for all buses to complete at
least totalTrips trips.


Example 1:
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.


Example 2:
Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.
 

Constraints:        1 <= time.length <= 10^5
                    1 <= time[i], totalTrips <= 10^7
Accepted:           36.4K
Submissions:        107.6K
Acceptance Rate:    33.8%
'''

from typing import List

class Solution:   # BruteForce T:(n ^ 2) TimeLimitExceeded   62 / 123 testcases passed
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        N = len(time)
        cur = time[0]
        while True:
            trips = 0
            for t in time:
                if cur < t: break
                else:
                    trips += cur // t
                    if trips >= totalTrips: return cur
            cur += 1

class Solution_BST:     # T:(n log(n))
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        minTime = min(time)
        maxTime = minTime * totalTrips
        def areAllTripsDone(timeCost) -> bool:
            numTripsDone = 0
            for t in time:
                numTripsDone += timeCost // t
            return numTripsDone >= totalTrips

        while minTime < maxTime:
            mid = (minTime + maxTime) >> 1
            if areAllTripsDone(mid): maxTime = mid
            else: minTime = mid + 1
        return minTime


'''     C++ | Easy Solution | 💯 Binary Search Approach | Heavily Commented

class Solution {
public:
    long long isSafe(vector<int>& time, long long val){
        long long a = 0;
        for(int i = 0; i < time.size(); i++){
            a += val / time[i];
        }
        return a;
    }
    long long minimumTime(vector<int>& time, int totalTrips) {
        //we will use Binary Search to find optimal ans
        //we will initialize the low to 1 and high to 1e14 
        //beacause we can have constraints 1e7*1e7
        long long low = 1, high = 1e14;
        
        //basic synatax of binary search
        while (low < high) {
            //finding mid with tackling the overflow
            long long mid = low + (high - low) / 2;
            
            //checking the trips possible with mid time the totalTrips 
            if (isSafe(time, mid) >= totalTrips) {
                //if safe the make high= mid
                high = mid;
            }
            else{
                //else make low to mid+1 as not found on mid
                low = mid + 1;
            }
        }
        //return the mid
        return low;
    }
};
'''

def main():
    sol = Solution()
    sol = Solution_BST()

    time, totalTrips = [1, 2, 3], 5 
#                       5, 2, 1   5
#                       4, 2, 1   4
            #           3  1, 1   3

    print(sol.minimumTime(time, totalTrips))       # Output: 3

    time, totalTrips = [2], 1
    print(sol.minimumTime(time, totalTrips))       # Output: 2

    time, totalTrips = [9, 3, 10, 5], 2
    print(sol.minimumTime(time, totalTrips))       # Output: 5

if __name__ == "__main__":
    main()
