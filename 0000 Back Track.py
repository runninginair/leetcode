class Box:
    def __init__(self) -> None:
        self.body = []
    
    def push(self, x:int) -> None:
        self.body.append(x)

    def pop(self) -> None:
        if self.body:
            self.body.pop(-1)

    def print(self) -> None:
        print('{', end='')
        for ele in self.body:
            print(ele, end=",")
        print("}")

class Solution:
    def print(self, A, i:int) -> None:
        print("{", end="")
        for j in range(i):
            print(A[j], end=",")
        print("}")
    
    def solve(self, A) -> None:
        N = len(A) if A else 0 # N = A == null? 0: A.legnth;
        for i in range(N+1):
            self.print(A, i)

    def solve2(self, A, i: int) -> None:
        N = len(A) if A else 0
        if (i > N): return
        self.print(A, i)
        self.solve2(A, i+1)

    # def solve3(self, A) -> None:
    #     box = Box()
    #     box.print()
    #     for a in A:
    #         box.push(a)
    #         box.print()
    def solve3(self, A, i, box):
        N = len(A) if A else 0
        box.print()
        if i >= N: return
        box.push(A[i])
        self.solve3(A, i+1, box)

    def solve4(self, A, i, box):
        N = len(A) if A else 0
        box.print()
        if i >= N: return

        box.push(A[i])
        self.solve4(A, i+1, box)
        box.pop()


def main():
    sol = Solution()
    A = [1, 2, 3]
    sol.solve(A)
    sol.solve2(A, 0)
    b = Box()
    sol.solve3(A, 0, b)
    
    b = Box()
    sol.solve4(A, 0, b)

    # Expect Output:
    # {}
    # {1}
    # {1, 2}
    # {1, 2, 3}
    

main()