'''
65. Valid Number
Hard    738     1301    Add to List     Share

A valid number can be split up into these components (in order):

    1. A decimal number or an integer.
    2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

    1. (Optional) A sign character (either '+' or '-').
    2. One of the following formats:
        1. One or more digits, followed by a dot '.'.
        2. One or more digits, followed by a dot '.', followed by one or more digits.
        3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

    1. (Optional) A sign character (either '+' or '-').
    2. One or more digits.

For example, all the following are valid numbers: 
    ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
    "+6e-1", "53.5e93", "-123.456e789"],

while the following are not valid numbers: 
    ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.


Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false


Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase),
digits (0-9), plus '+', minus '-', or dot '.'.

Accepted:       288,340
Submissions:    1,556,532
'''

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        DIGITS = ('0','1','2','3','4','5','6','7','8','9')
        SIGNS = ('+', '-')
        n = len(s)
        if n == 1:
            return True if s in DIGITS else False

        has_digit, has_e, num_of_dot, num_of_e = False, False, 0, 0
        for i in range(n):
            if s[i] == '.':
                num_of_dot += 1
                if num_of_dot > 1:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                has_e = True
                num_of_e += 1
                if num_of_e > 1:
                    return False
            elif ((ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')) 
                or (ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'))):
                return False
            elif s[i] in DIGITS:
                has_digit = True
        if not has_digit:
            return False
        
        # A helper function to verify if s is a valid number.
        def isValidNumber(s: str) -> bool:
            if s == '':
                return True
            if s == '+' or s == '-' or s == '.':
                return False
            for i in range(len(s)):
                if i == 0 and s[i] in SIGNS:
                    continue
                if s[i] in DIGITS or s[i] == '.':
                    continue
                else:
                    return False
            return True

        # A helper function to verify if s is a valid integer.
        def isValidInteger(s: str) -> bool:
            if s == '':
                return True
            if s == '+' or s == '-':
                return False
            for i in range(len(s)):
                if i == 0 and s[i] in SIGNS:
                    continue
                if s[i] not in DIGITS:
                    return False
            return True

        if has_e:
            spl = re.split('e|E', s)
            if '' in spl :
                return False
            return isValidInteger(spl[1]) and isValidNumber(spl[0])
            
        else:
            return isValidNumber(s)

                    
def main():
    sol = Solution()

    arr = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for a in arr:
        print(sol.isNumber(a), end=',')     # Output: True
    print()

    arr = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "+."]
    for a in arr:
        print(sol.isNumber(a), end=',')     # Output: False
    print()

if __name__ == "__main__":
    main()
