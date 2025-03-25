class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        max_streak = 1

        for num in nums_set:

            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                max_streak = max(current_streak, max_streak)

            

        return max_streak

# Time Complexity: O(N)
# Space Complexity: O(N)