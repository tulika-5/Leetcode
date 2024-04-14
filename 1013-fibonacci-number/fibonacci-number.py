class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        f1, f2 = 0, 1
        for _ in range(2, n + 1):
            f1, f2 = f2, f1 + f2
        return f2

