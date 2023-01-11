'''
0007. Reverse Integer
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        sign, res = 1, 0
        if x < 0:
            sign = -1
            x *= -1
        while x != 0:
            t = x - x // 10 * 10
            res = res*10 + t
            x //= 10
        if res > 2 ** 31: return 0
        else: return res*sign


def main():
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))

main()
