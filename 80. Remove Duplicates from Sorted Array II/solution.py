class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        for i, x in enumerate(nums):
            count = nums.count(nums[i])
            if count > 2:
                for j in range(count-2):
                    nums.remove(x)

        return len(nums)