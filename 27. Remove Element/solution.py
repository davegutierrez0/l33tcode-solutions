class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        n = len(nums)

        while i < n:
            if nums[i] == val:
                # Replace current val with the last element
                nums[i] = nums[n - 1]
                # Decrease the size of "valid" array
                n -= 1
            else:
                # Move to next index only if no removal
                i += 1

        return n


# Time Complexity: O(N)
# Space Complexity: O(1)

# Swap with the last element if it matches.
# Shrink the effective length of the array.
# Only increment i when you don’t remove.
# Don’t care about order, just care about who stays.