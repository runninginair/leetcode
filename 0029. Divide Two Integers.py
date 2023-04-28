''' 29. Divide Two Integers

Medium      4K      12.8K       Companies

Given two integers dividend and divisor, divide two integers without
using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store
integers within the 32-bit signed integer range: [ -2^31, 2^31 - 1].
For this problem, if the quotient is strictly greater than 2^31 - 1, then
return 2^31 - 1, and if the quotient is strictly less than -2^31, then
return -2^31.


Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:        -2^31 <= dividend, divisor <= 2^31 - 1
                    divisor != 0
Accepted:           584.8K
Submissions:        3.4M
Acceptance Rate:    17.2%

'''


class Solution_illegal:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            res = dividend // divisor
        elif divisor < 0:
            res = -(dividend // -divisor)
        else:
            res = -(-dividend // divisor)
        res = min(res, 2 ** 31 - 1)
        res = max(res, -(2 ** 31))
        return res


class Solution:     ### TLE    T: O(n), n = dividend
    def divide(self, dividend: int, divisor: int) -> int:
        res, negative = -1, True
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            negative = False
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        while dividend >= 0:
            dividend -= divisor
            res += 1
        return -res if negative else res


class Solution_range:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend >= 0 and divisor <
                      0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result


'''     Really simple O(log(n)) solution with explanation (Java)

class Solution {
    public int divide(int dividend, int divisor) {
        
        // Edge cases
        // If the quotient is stictly greater than 2^31-1, return 2^31-1
        if((dividend == Integer.MIN_VALUE && divisor == -1) 
           || (dividend == Integer.MAX_VALUE && divisor == 1)){
            return Integer.MAX_VALUE;
        }
        
		// This is used to determine if the final result is -ve
        boolean isPositive = true;
        
        // If dividend and divisor have different symbols, the result is -ve
        if((dividend <0) ^ (divisor < 0)){
            isPositive = false;
        }
        
        // In order to not have to deal with numbers with different sings, lets convert
        // both divisor and dividend to integers
        
        dividend = dividend < 0 ? dividend : -1* dividend;
        divisor = divisor < 0? divisor: -1*divisor;
        
        // Each time we do a left shift of a number, it is same as doubling it
        // Similarly, a right shift equates to shrinking that number by half. 
        // The logic is
        // step1: for i in range(31,0):
        // step2:      is divisor * 2^i >= dividend? (Remmeber, both number are -ve)
        // step3:      Yes: dividend = dividend - divisor * 2^i
        // step4:     No: continue checking
        
        // One problem with that logic is the possibility of integer overflow in step 2.
        // Example:
        //  For the sake of simplicity, lets assume:
        //      int is a 8 bit signed integer (i.e. int holds values between 2^7-1 & -2^7 (i.e. 127 and -128)),
        //      Also assume, divisor = 3, dividend = 127
        //  Now, in step 2, 3 * 2 ^ 7 is 474 which greater than 127. 
        // So, we need to find the highest power of 2 that can prevent overflow instead of iterating from 31
        
        int highestPower = findHighestPower(divisor, dividend);
        
        int numMultiply = 0;
        for(int i=highestPower; i>=0; i--){
            
            if((divisor << i) >=  dividend){
                dividend = dividend - (divisor << i);
                numMultiply += (1<<i);
            }
            
        }
        
        if(isPositive){
            return numMultiply;
        }
        return -1*numMultiply;
        
    }
    
    int findHighestPower(int divisor, int dividend){
        
        // In order to find the highest power, keep doubling the dividend
        // as long as it is greater than half of divisor (Remember, both numbers are -ve). 
        // Because if you double after that, it is going to be less than divisor
        
        int halfDividend = dividend >>1;
        int highestPower = 0;
        while(divisor >= halfDividend){
            highestPower++;
            divisor = divisor << 1;
        }
        return highestPower;
        
    }

}
'''


def main():
    sol = Solution_illegal()
    sol = Solution()
    sol = Solution_range()

    dividend, divisor = 10, 3      # Output: 3
    print(sol.divide(dividend, divisor))

    dividend, divisor = 7, -3      # Output: -2
    print(sol.divide(dividend, divisor))

    dividend, divisor = -2147483648, -1      # Output: 2147483647
    print(sol.divide(dividend, divisor))


if __name__ == "__main__":
    main()
