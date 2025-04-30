from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0 

        for j in range(1,len(nums)):
            if nums[i] !=  nums[j]:
                i += 1
                nums[i] = nums[j]



        return i+1


class Solution:
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write-1]:
            nums[write] = nums[read]
            write +=1 

    return write

# Time Complexity: O(N)
# Space Complexity: O(1)
# Mnemonic: “Two-Finger Scan”
#   Two-Finger = two pointers (read and write).
# 	Scan = you scan once through the list.

# Picture yourself dragging one finger (“read”) along the sorted row of numbers, and tapping with the other
# finger (“write”) only when you see a new unique. That one-pass, two-finger motion is O(N) time and uses 
# just those two fingers—O(1) space.