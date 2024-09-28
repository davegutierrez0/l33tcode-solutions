class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        numsSet = set(nums)

        for x in numsSet:
            if nums.count(x) > (len(nums) / 2):
                return(x)
