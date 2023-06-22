''' 0837. New 21 Game

Medium      1.3K      879       Companies

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points.
During each draw, she gains an integer number of points randomly from the range
[1, maxPts], where maxPts is an integer. Each draw is independent and the
outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.


Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.


Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.


Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:            0 <= k <= n <= 10^4
                        1 <= maxPts <= 10^4
Accepted:               40.1K
Submissions:            105.3K
Acceptance Rate:        38.1%
'''


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        windowSum = 1.0
        probability = 0.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts
            
            if i < k:
                windowSum += dp[i]
            else:
                probability += dp[i]
            
            if i >= maxPts:
                windowSum -= dp[i - maxPts]
        
        return probability
    
def main():
    sol = Solution()

    n, k, maxPts = 10, 1, 10    # Output: 1.00000
    print(sol.new21Game(n, k, maxPts))

    n, k, maxPts = 6, 1, 10     # Output: 0.60000
    print(sol.new21Game(n, k, maxPts))

    n, k, maxPts = 21, 17, 10   # Output: 0.73278
    print(sol.new21Game(n, k, maxPts))

    ### 1,  2,  3,  4,  5,  6,  7,  8,  9,  10      21 - 17 = 4
    ###
    ### 1,  2,  3,  4,  5,  6,  7,  8,  9,  10  
    ###
    ### 1,  2,  3,  4,  5,  6,  7,  8,  9,  10  

    ### 1,  2,  3,  4,  5,  6,  7,  8,  9,  10  

    ### 1,  2,  3,  4,  5,  6,  7,  8,  9,  10  


if __name__ == "__main__":
    main()