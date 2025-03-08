class Solution:
    def fib(self, n: int) -> int:
        # F(0) and F(1) are equal to input
        if n < 2:
            return n

        # Base cases of F(0) and F(1) are prev and current
        prev, curr = 0, 1

        # Starting at F(2)
        for _ in range(2,n+1):
            prev, curr = curr, prev + curr

        return curr
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)