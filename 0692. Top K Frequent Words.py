''' 692. Top K Frequent Words
Medium      5344    280     Add to List     Share
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the
words with the same frequency by their lexicographical order.


Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:    1 <= words.length <= 500
                1 <= words[i].length <= 10
                words[i] consists of lowercase English letters.
                k is in the range [1, The number of unique words[i]]
 
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

Accepted:       440,306
Submissions:    796,110
'''

import collections
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.OrderedDict()
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        # print(dic)
        # dic.sort(key = lambda x: x = dic[y], reverse = True)
        # lis = (list(dic)).sort(key = lambda x: dic[x], reverse = True)
        lis, res, i = [], [], 0
        for word in dic:
            lis.append([dic[word], word])
        lis.sort(key = lambda x:x[0], reverse=True)
        for i in range(k):
            res.append(lis[i][1])
        return res


def main():
    sol = Solution()
    words, k = ["i","love","leetcode","i","love","coding"], 2  # Output: ["i","love"]
    print(sol.topKFrequent(words, k))

main()
