''' 509. Fibonacci Number
Easy    5646    301     Add to List     Share

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

 * F(0) = 0, F(1) = 1
 * F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).


Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:    0 <= n <= 30
Accepted:       1,137,399
Submissions:    1,642,745
'''


class Solution_v0:      ### Original Solution     T: O(2^n)  M: O(2^n)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n - 1) + self.fib(n - 2)

class Solution_v1_1:    ### DP solution 1     T: O(n) M:O(n)
    def fib(self, n: int) -> int:
        if n < 2: return n
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range (2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class Solution_v1_2:    ### DP solution 2     T: O(n) M:O(1)
    def fib(self, n: int) -> int:
        if n < 2: return n
        dp, index = [0, 1, 1], -1
        for i in range (3, n + 1):
            index = i % 3
            dp[index] = dp[index - 1] + dp[index - 2]
        return dp[index]

from functools import lru_cache
class Solution_v2_1:  ### Cache Solution    # T: O(n)  M: O(n)
    @lru_cache(maxsize = None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n - 1) + self.fib(n - 2)


# class Solution_v2_2:  ### Cache Solution_2    # T: O(n)  M: O(n)
my_dict = dict()

def my_cache(fun):
    def wrap(*args, **kwargs):
        key = args[0]
        if key not in my_dict: 
            my_dict[key] = fun(*args, **kwargs)
        return my_dict[key]
    return wrap

@my_cache
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

class Solution_v3:  ### Tail Recursion Solution    # T: O(n)  M: O(n)
    ''' About fib_tail_recursion
        num -       就是 n, 也就是 fib 数列的第 n 项。
        result -    是我们最后求得的结果
        temp -      一个暂时存放的数字（从 1 开始）。
    '''
    def fib(self, n: int) -> int:
        def fib_tail_recursion(num, result, temp):
            if num == 0: return result
            else: return fib_tail_recursion(num - 1, temp, result + temp)
        return fib_tail_recursion(n, 0, 1)

        
class Solution_v4:  ### Iteration Solution    # T: O(n)  M: O(1)
    def fib(self, n: int) -> int:
        res, temp = 0, 1
        for _ in range(n):
            res, temp = temp, temp + res
        return res

def main():
    sol = Solution_v0()     ### Will calculate very slow after 30
    sol = Solution_v1_1()   ### DP
    sol = Solution_v1_2()
    sol = Solution_v2_1()   ### Cache
    sol = Solution_v3()     ### Tail Recursion
    sol = Solution_v4()     ### Iteration solution   # T: O(n)  M: O(1)

    for i in range(35): print("The {}-th fib number = {}".format(i, sol.fib(i)), end='\n')

    # for i in range(35): print("The {}-th fib number = {}".format(i, fib(i)), end='\n')
    # for i in range(5): print("The {}-th fib number = {}".format(i, fib(i)), end='\n')


if __name__ == "__main__":
    main()
