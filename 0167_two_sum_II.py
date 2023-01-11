'''
167. Two Sum II - Input Array Is Sorted
Medium
'''

class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target: int): # O(n) solution
        # Init two pointers front(f) and rear(r)
        f, r = 0, len(numbers) - 1
        while (f < r):
            if numbers[f] + numbers[r] == target:
                return [f + 1, r + 1]
            elif numbers[f] + numbers[r] < target: 
                f += 1
            else:
                r -= 1


def main():
    s = Solution()

    # Input: Output: [1,2]
    numbers = [2,7,11,15]
    target = 9
    print(s.twoSum(numbers, target))




main()
