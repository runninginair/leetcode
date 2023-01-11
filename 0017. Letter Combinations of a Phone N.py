''' 17. Letter Combinations of a Phone Number
Medium  12846   766 Add to List Share

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

              1               2               3
        (           ),  ('a','b','c'),  ('d','e','f'),

              4               5               6
        ('g','h','i'),  ('j','k','l'),  ('m','n','o'),

              7               8               9
    ('p','q','r','s'),  ('t','u','v'),  ('w','x','y','z')

              *               0               #
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:    0 <= digits.length <= 4
                digits[i] is a digit in the range ['2', '9'].
Accepted:       1,381,876
Submissions:    2,491,632
'''

class Solution:
    ''' T(n) -> O(4^m * 3^n)    m is number of 7,9; n is number of others.
        S(n) -> O(L)            L is the length of digits.
    '''
    def letterCombinations(self, digits: str):
        if not digits or digits == "":
            return []
        LETTER = [(), (), ('a','b','c'), ('d','e','f'), ('g','h','i'), ('j','k','l'),
                  ('m','n','o'), ('p','q','r','s'), ('t','u','v'), ('w','x','y','z')]
        
        def backtrack(lis, k, cur):
            if len(cur) >= len(digits):
                res.append("".join(cur.copy()))
                return
  
            for ch in lis[k]:
                cur.append(ch)
                backtrack(lis, k+1 ,cur)
                cur.pop()

        res, lis = [], []
        for d in digits:
            lis.append(LETTER[int(d)])
        # print(lis)
        backtrack(lis, 0, [])
        return res


def main():
    sol = Solution()
    print(sol.letterCombinations('23'))
    # print(sol.letterCombinations('999'))

main()
