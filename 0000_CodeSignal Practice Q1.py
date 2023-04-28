'''     CodeSignal Practice     Q.1

Given an array of integers a, your task is to calculate the digits that occur
the most number of times in the array. Return the array of these digits in
ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
Here are the number of times each digit appears in the array:
0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits
which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].


Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of positive integers.

Guaranteed constraints:     1 ≤ a.length ≤ 10^3,
                            1 ≤ a[i] < 100.

[output] array.integer:
    The array of most frequently occurring digits, sorted in ascending order.

[Python 3] Syntax Tips:

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''

### Passed Score: 500/500
def solution(a):
    cnt = [0 for _ in range(10)]
    for num in a:
        for c in str(num):
            cnt[int(c)] += 1
    most = max(cnt)
    res = []
    for i in range(10):
        if cnt[i] == most:
            res.append(i)
    return res
