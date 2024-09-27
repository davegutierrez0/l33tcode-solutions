class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:
            nums.remove(val)
        
        nums.sort()
        
        return len(nums)
    
    # n^2 solution - come back to this 