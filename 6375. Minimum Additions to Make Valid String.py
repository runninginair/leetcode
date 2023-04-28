''' 6375. Minimum Additions to Make Valid String
User Accepted:2325
User Tried:3647
Total Accepted:2348
Total Submissions:5051
Difficulty:Medium
Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

'''

class Solution:
    def addMinimum(self, word: str) -> int:
        ans = i = tail = 0
        map = "abc"
        for char in word:
            if char != map[i]:
                while char != map[i]:
                    i = (i + 1) % 3
                    ans += 1
            i = (i + 1) % 3
        if word[-1] == 'a': tail = 2
        elif word[-1] == 'b': tail = 1
        return ans + tail


def main():
    sol = Solution()

    word = "aaa"
    print(sol.addMinimum(word))

main()



