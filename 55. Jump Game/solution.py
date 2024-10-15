from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target_index = len(nums) - 1
        
        max_index = 0 # Start at 0 index
        
        if target_index == max_index: 
            return True # Case where we are already on the target (single item in list)
        
        for idx, num in enumerate(nums):
            
            if idx > max_index:
                return False # Case where current index is unreachable
            
            max_index = max(max_index, idx + num) # Update furthest possible reach (max function helps if nums[idx] == 0)

            if max_index >= target_index:
                return True # If we can meet or exceed the last index
        
        return False # Default case assumes we cannot get to target_index
        
        
# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump(nums = [2,3,1,1,4]))    
    print(solution.canJump(nums = [3,2,1,0,4]))
    print(solution.canJump(nums =[0]))
    print(solution.canJump(nums =[3,0,8,2,0,0,1]))
    
# Time Complexity: O(n)
# Space Complexity: O(1)