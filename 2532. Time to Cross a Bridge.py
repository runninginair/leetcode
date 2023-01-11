''' 2532. Time to Cross a Bridge

Hard    48    128    Companies

There are k workers who want to move n boxes from an old warehouse to a new one.
You are given the two integers n and k, and a 2D integer array time of size
k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].

The warehouses are separated by a river and connected by a bridge.
The old warehouse is on the right bank of the river, and the new warehouse is
on the left bank of the river.
Initially, all k workers are waiting on the left side of the bridge.
To move the boxes, the ith worker (0-indexed) can :

 * Cross the bridge from the left bank (new warehouse) to the right bank
   (old warehouse) in leftToRighti minutes.
 * Pick a box from the old warehouse and return to the bridge in pickOldi minutes.
   Different workers can pick up their boxes simultaneously.
 * Cross the bridge from the right bank (old warehouse) to the left bank
   (new warehouse) in rightToLefti minutes.
 * Put the box in the new warehouse and return to the bridge in putNewi minutes.
   Different workers can put their boxes simultaneously.

A worker i is less efficient than a worker j if either condition is met:

 * leftToRighti + rightToLefti > leftToRightj + rightToLeftj
 * leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j

The following rules regulate the movement of the workers through the bridge :

 * If a worker x reaches the bridge while another worker y is crossing the bridge,
   x waits at their side of the bridge.
 * If the bridge is free, the worker waiting on the right side of the bridge
   gets to cross the bridge. If more than one worker is waiting on the right
   side, the one with the lowest efficiency crosses first.
 * If the bridge is free and no worker is waiting on the right side, and at least
   one box remains at the old warehouse, the worker on the left side of the river
   gets to cross the bridge. If more than one worker is waiting on the left side,
   the one with the lowest efficiency crosses first.
 * Return the instance of time at which the last worker reaches the left bank of
   the river after all n boxes have been put in the new warehouse.


Example 1:

Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
Output: 6
Explanation: 
From 0 to 1: worker 2 crosses the bridge from the left bank to the right bank.
From 1 to 2: worker 2 picks up a box from the old warehouse.
From 2 to 6: worker 2 crosses the bridge from the right bank to the left bank.
From 6 to 7: worker 2 puts a box at the new warehouse.

The whole process ends after 7 minutes. We return 6 because the problem asks for
the instance of time at which the last worker reaches the left bank.


Example 2:
Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
Output: 50
Explanation: 
From 0  to 10: worker 1 crosses the bridge from the left bank to the right bank.
From 10 to 20: worker 1 picks up a box from the old warehouse.
From 10 to 11: worker 0 crosses the bridge from the left bank to the right bank.
From 11 to 20: worker 0 picks up a box from the old warehouse.
From 20 to 30: worker 1 crosses the bridge from the right bank to the left bank.
From 30 to 40: worker 1 puts a box at the new warehouse.
From 30 to 31: worker 0 crosses the bridge from the right bank to the left bank.
From 31 to 39: worker 0 puts a box at the new warehouse.
From 39 to 40: worker 0 crosses the bridge from the left bank to the right bank.
From 40 to 49: worker 0 picks up a box from the old warehouse.
From 49 to 50: worker 0 crosses the bridge from the right bank to the left bank.
From 50 to 58: worker 0 puts a box at the new warehouse.

The whole process ends after 58 minutes. We return 50 because the problem asks for
the instance of time at which the last worker reaches the left bank.
 

Constraints:        1 <= n, k <= 10^4
                    time.length == k
                    time[i].length == 4
                    1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000
Accepted:           1.8K
Submissions:        3.6K
Acceptance Rate:    50.7%
'''

import heapq, math
from typing import List

class Solution: ### My Solution NOT correct.
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        hp_left, hp_right = [], []
        for i, t in enumerate(time):
            hp_left.append([-(t[1] + t[3]), -i, t[0], t[1], t[2], t[3]])
        heapq.heapify(hp_left)
        for worker in hp_left: print(worker)

        time, free = [], True
        while free and n > 0 and hp_left:
            left_worker = heapq.heappop(hp_left)
            n -= 1
            time.append(worker[2])
            print("# 1:", time)
            heapq.heappush(hp_right, worker)
            while hp_right:
                worker = heapq.heappop(hp_right)
                if n > 0 and hp_left: break
                time[-1] = max(time[-1], worker[3])
                print("# 2:", time)

                time.append(worker[3])
                time.append(worker[4])
                print("# 3:", time)

                heapq.heappush(hp_left, worker)

        return sum(time)


class Solution_v0: ### LeetCode ID: ye15
    '''     Intuition
            Here, we maintain 4 prioirty queues.

            l  -- ready to join the queue ll once the time allows
            ll -- ready to cross the bridge from left to right
            r  -- ready to join the queue rr once the time allows
            rr -- ready to cross the bridge from right to left
    '''
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        ans = free = 0 
        l, ll, r, rr = [], [], [], []
        for i, (x, _, y, _) in enumerate(time): heapq.heappush(ll, (-x-y, -i))
        
        while n or r or rr: 
            if not rr and (not r or r[0][0] > free) and (not n or not ll and (not l or l[0][0] > free)): 
                cand = math.inf 
                if n and l: cand = min(cand, l[0][0])
                if r: cand = min(cand, r[0][0])
                free = cand

            while r and r[0][0] <= free: 
                _, i = heapq.heappop(r)
                heapq.heappush(rr, (-time[i][0] - time[i][2], -i))

            while l and l[0][0] <= free: 
                _, i = heapq.heappop(l)
                heapq.heappush(ll, (-time[i][0] - time[i][2], -i))

            if rr:
                _, i = heapq.heappop(rr)
                free += time[-i][2]
                if n: heapq.heappush(l, (free + time[-i][3], -i))
                else: ans = max(ans, free)
            else: 
                _, i = heapq.heappop(ll)
                free += time[-i][0]
                heapq.heappush(r, (free + time[-i][1], -i))
                n -= 1
        return ans 

def main():
    sol = Solution()
    sol = Solution_v0()

    n, k, time = 1, 3, [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]    # Output: 6
    print(sol.findCrossingTime(n, k, time))

    n, k, time = 3, 2, [[1, 9, 1, 8], [10, 10, 10, 10]]              # Output: 50
    print(sol.findCrossingTime(n, k, time))


if __name__ == "__main__":
    main()
