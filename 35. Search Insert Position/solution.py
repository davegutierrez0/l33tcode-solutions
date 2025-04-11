class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] < target:
                left = middle + 1
            
            else: 
                right = middle - 1

        return left # Left is the insertion position

# Time Complexity: O(log N)
# Space Complexity: O(1)
# Mnemonic: Cut, Compare, Shift — “T > M? Then L jumps past M!”