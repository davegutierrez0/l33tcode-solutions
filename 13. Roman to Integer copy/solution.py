from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0

        while i < len(nums) - 1:
            firstNumber = nums[i]
            secondNumber = target - firstNumber

            if secondNumber in nums[i+1:]:
                return [i] + [nums[i+1:].index(secondNumber)+(i+1)]
            
            else:
                i +=1
