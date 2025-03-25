class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_sorted = sorted(nums)

        max_streak = 1
        current_streak = 1

        for i in range(1,len(nums_sorted)):

            if nums_sorted[i] == nums_sorted[i-1] + 1:
                current_streak += 1
                max_streak = max(current_streak, max_streak)
            elif nums_sorted[i] == nums_sorted[i-1]:
                pass
            else:
                current_streak = 1
            

        return max_streak

# Time Complexity: O(N log N) — due to sorting
# Space Complexity: O(N) — for storing the sorted list