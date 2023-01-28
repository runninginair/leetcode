''' 787. Cheapest Flights Within K Stops

Medium      6.7K      300       Companies

There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price
from src to dst with at most k stops. If there is no such route, return -1.


Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
       src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has
cost 100 + 600 = 700. Note that the path through cities [0,1,2,3] is cheaper
but is invalid because it uses 2 stops.


Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has
cost 100 + 100 = 200.


Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:        1 <= n <= 100
                    0 <= flights.length <= (n * (n - 1) / 2)
                    flights[i].length == 3
                    0 <= from-i, to-i < n
                    from-i != to-i
                    1 <= price-i <= 10^4
                    There will not be any multiple flights between two cities.
                    0 <= src, dst, k < n
                    src != dst
Accepted:           309.9K
Submissions:        859.7K
Acceptance Rate:    36.0%
'''

from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b, p in flights:
            adj[a].append([b, p, 1])
        for ad in adj: print(ad)

        return math.inf

### Official Solution:
### https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/2825208/cheapest-flights-within-k-stops/


def main():
    sol = Solution()
    
    n, flights, src, dst, k = 4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))           # Output: 700


if __name__ == "__main__":
    main()
