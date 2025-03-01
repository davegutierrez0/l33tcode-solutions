class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 1, 2

        for _ in range(3,n+1):
            prev, curr = curr, prev + curr
        return curr
    
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)