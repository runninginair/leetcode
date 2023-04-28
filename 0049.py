class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        n, res, dic = len(strs), [], {}
        if n == 1:
            return [strs]
        for word in strs:
            k = []
            for i in range(len(word)):
                k.append(word[i])
            k.sort()
            d = "".join(k)
            if d not in dic.keys():
                dic[d] = [word]
            else:
                dic[d].append(word)
        for k in dic.keys():
            res.append(dic[k])
        return res

def main():
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))

main()
