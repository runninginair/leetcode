'''     Q.2     Practice for Netflix OA

Given an array of positive integers a, your task is to calculate the sum of
every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the
string representations of a[i] and a[j] respectively.


Example:

For a = [10, 2], the output should be solution(a) = 1344.
a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.


For a = [8], the output should be solution(a) = 88.
There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88,
so the answer is 88.


For a = [1, 2, 3], the output should be solution(a) = 198.
a[0] ∘ a[0] = 1 ∘ 1 = 11,
a[0] ∘ a[1] = 1 ∘ 2 = 12,
a[0] ∘ a[2] = 1 ∘ 3 = 13,
a[1] ∘ a[0] = 2 ∘ 1 = 21,
a[1] ∘ a[1] = 2 ∘ 2 = 22,
a[1] ∘ a[2] = 2 ∘ 3 = 23,
a[2] ∘ a[0] = 3 ∘ 1 = 31,
a[2] ∘ a[1] = 3 ∘ 2 = 32,
a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.


Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer a

A non-empty array of positive integers.

Guaranteed constraints:     
    
    1 ≤ a.length ≤ 10^5,
    1 ≤ a[i] ≤ 10^6.

[output] integer64

    The sum of all a[i] ∘ a[j]s.
    It's guaranteed that the answer is less than 2^53.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string

def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

'''
### Brute force solution  O(n^2)   TLE
# def solution(arr):
#     res = 0
#     for n1 in arr:
#         for n2 in arr:
#             res += int(str(n1) + str(n2))
#     return res


def solution(arr):      # T: O(n)
    N, lowSum = len(arr), sum(arr)
    ans = lowSum * N
    print("lowSum =", lowSum, "  ans =", ans)

    for i in range(N):
        size = len(str(arr[i]))
        print(lowSum * 10 ** size)
        ans += lowSum * 10 ** size
        print("i =", i, " size =",size, " ans =", ans)
    return ans


def main():
    print(solution([10, 2]), end="\n\n")        ### Output: 1344
    # print(solution([8]), end="\n\n")            ### Output: 88
    # print(solution([1, 2, 3]), end="\n\n")      ### Output: 198

    # print(solution([2, 30, 400]), end="\n\n")   ### Output: 480816
    # print(solution([2, 11, 700, 3000]), end="\n\n")   ### Output: 41266282

main()
