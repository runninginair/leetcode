'''
Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations:
add and find.
add- Add the number to an internal data structure.
find- Find if there exists any pair of numbers which sum is equal to the value.

Example 1:
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:
add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''


class Solution:
    dic = {}
    def add(self, number: int):
        self.dic.update({len(self.dic): number})
    
    def find(self, target: int):
        for i, _ in enumerate(self.dic):
            print("key =", i, "  value =", self.dic[i])
            diff = target - self.dic[i]
            if diff in self.dic.values() and i != self.dic.get(diff): return True
        return False


def main():
    sol = Solution()
    sol.add(1)
    sol.add(3)
    sol.add(5)
    print(sol.dic)
    print(sol.find(4))
    print(sol.find(7))

    sol.dic.clear()
    
    sol_2 = Solution()
    sol_2.add(1)
    sol_2.add(3)
    sol_2.add(5)
    sol_2.add(5)
    print(sol_2.dic)
    print(sol_2.find(9))
    print(sol_2.find(10))


main()
