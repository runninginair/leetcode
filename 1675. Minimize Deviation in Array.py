''' 1675. Minimize Deviation in Array

Hard    2.2K    117     Companies

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

 * If the element is even, divide it by 2.

    For example, if the array is [1,2,3,4], then you can do this operation on the last
    element, and the array will be [1,2,3,2].

 * If the element is odd, multiply it by 2.

    For example, if the array is [1,2,3,4], then you can do this operation on the first
    element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.


Example 1:
Input: nums = [1, 2, 3, 4]
Output: 1
Explanation:    You can transform the array to [1, 2, 3, 2], then to [2, 2, 3, 2],
                then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4, 1, 5, 20, 3]
Output: 3
Explanation:    You can transform the array after two operations to [4, 2, 5, 5, 3],
                then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3
 
Constraints:        n == nums.length
                    2 <= n <= 5 * 10^4
                    1 <= nums[i] <= 10^9
Accepted:           58.9K
Submissions:        111.1K
Acceptance Rate:    53.0%
'''

from typing import List
import heapq, math

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        priorityQueue, minNum, minDeviation = [], math.inf, math.inf
        for num in nums:
            if num & 1: num <<= 1
            heapq.heappush(priorityQueue, -num)
            minNum = min(minNum, num)

        # print(priorityQueue, minNum)
        while priorityQueue:
            maxNum = -1 * heapq.heappop(priorityQueue)
            minDeviation = min(minDeviation, maxNum-minNum)
            if maxNum & 1: break
            maxNum >>= 1
            minNum = min(minNum, maxNum)
            heapq.heappush(priorityQueue, -maxNum)
        # print(priorityQueue, minNum)
        return minDeviation

''' 
class Solution {
    public int minimumDeviation(int[] nums) {
        PriorityQueue<Integer> pq=new PriorityQueue<>(Collections.reverseOrder());
        int minValue=Integer.MAX_VALUE;
        for(int x:nums){
            if((x&1)==1)
                x<<=1;
            pq.add(x);
            minValue=Math.min(minValue,x);
        }
        int minDeviation=Integer.MAX_VALUE;
        while(!pq.isEmpty()){
            int curr=pq.poll();
            minDeviation=Math.min(minDeviation,curr-minValue);
            if((curr&1)==1)
                break;
            curr>>=1;
            minValue=Math.min(minValue,curr);
            pq.add(curr);
        }
        return minDeviation;
    }
}
'''


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.minimumDeviation(nums)) # Expect Output: 1

    nums = [4, 1, 5, 20, 3]
    print(sol.minimumDeviation(nums)) # Expect Output: 3

    nums = [2, 10, 8]
    print(sol.minimumDeviation(nums)) # Expect Output: 3

    nums = [4, 10, 40, 20, 24]
    print(sol.minimumDeviation(nums)) # Expect Output: 1

    nums = [3, 5]
    print(sol.minimumDeviation(nums)) # Expect Output: 1

    nums =  [10, 4, 3]
    print(sol.minimumDeviation(nums)) # Expect Output: 2


if __name__ == "__main__":
    main()
