from collections import Counter 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0

        zero_count = 0

        while n > 0:
            n //= 5
            zero_count += n
        return zero_count

# Time Complexity: (O(log(n)))
# Space Complexity: O(1)