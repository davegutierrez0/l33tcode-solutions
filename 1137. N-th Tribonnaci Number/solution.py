class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        if n == 2:
            return 1
        
        a = 0
        b = 1
        c = 1

        for _ in range(n-2):
            a, b, c = b, c, a + b + c

        return c
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)