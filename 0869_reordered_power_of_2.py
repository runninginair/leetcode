'''
869. Reordered Power of 2
'''
import collections

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        S = set()
        num = 1
        while num <= 10**9:
            str_num = str(num)
            list_num = sorted(str_num, reverse=True)
            str_num = ''.join(list_num)
            # print(str_n)
            numInSet = int(str_num)
            S.add(numInSet)
            num *= 2
        # print(s)
        # print(len(s))

        str_n = str(n)
        list_n = sorted(str_n, reverse = True)
        str_n = ''.join(list_n)
        sorted_n = int(str_n)

        return sorted_n in S


def main():
    s = Solution()
    print(s.reorderedPowerOf2(10)) # False
    print(s.reorderedPowerOf2(1))  # True 

main()


