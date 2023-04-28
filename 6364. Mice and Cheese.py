''' 6364. Mice and Cheese

'''
import heapq
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        N, res = len(reward1), 0
        hp = [[0, 0, 0] for _ in range(N)]
        for i in range(N):
            hp[i][0] = -(reward1[i] - reward2[i])
            hp[i][1], hp[i][2] = reward1[i], reward2[i]
        for h in hp: print(h)
        heapq.heapify(hp)
        for _ in range(k):
            res += heapq.heappop(hp)[1]
        while hp:
            res += heapq.heappop(hp)[2]
        return res


def main():
    sol = Solution()

    reward1 = [1,1,3,4]
    reward2 = [4,4,1,1]
    k = 2 #Output: 15

    print(sol.miceAndCheese(reward1, reward2, k))

main()