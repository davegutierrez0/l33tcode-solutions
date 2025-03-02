class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        
        # Could use @lru_cache(maxsize=None) (`or @caching in LC``) here to auto-memoize
        def robFrom(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            haul = max(robFrom(i+1), robFrom(i+2) + nums[i])

            memo[i] = haul

            return haul

        return robFrom(0)
        
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)