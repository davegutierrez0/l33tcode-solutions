from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j =  1
        
        while i < j and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                while j < len(nums) and nums[j] == 0:
                    j += 1
                i += 1
            
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
                while j < len(nums) and nums[j] == 0:
                    j+=1
                    
            elif nums[i] == 0 and nums[j] == 0:
                while j< len(nums) and nums [j] == 0:
                    j+=1
            
            else: 
                i += 1
                j += 1
            
        print(nums)
    

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes(nums = [0,1,0,3,12]))
    print(solution.moveZeroes(nums = [0]))
    print(solution.moveZeroes(nums = [0,0,1]))

    
