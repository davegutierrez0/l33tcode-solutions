from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if (len(nums)) == 1:
            return 0
        
        target_index = len(nums) - 1
        
        jumps = 0
        
        # Starting position
        max_index = 0
        
        # Wait for iteration to get to the max_index
        current_end = 0
        
        for i, num in enumerate(nums):
            max_index = max(max_index, i + num)
            
            last_possible_moment = 0
            for j, next_num in enumerate(nums[i+1:num+1]):
                
                last_possible_moment = j if next_num > last_possible_moment else last_possible_moment
                

                
            if i == current_end:
                jumps += 1
                current_end = max_index
                
                if current_end >= target_index:
                    return jumps

        
        
# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.jump(nums =  [2,3,1,1,4]))    
    print(solution.jump(nums = [2,3,0,1,4]))
    print(solution.jump(nums = [1,2,1,1,1]))
    
# Time Complexity: O(n)
# Space Complexity: O(1)