from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start with two pointers at ends of the array
        len_height = len(height)
        left, right = 0, len_height - 1        
        max_area = 0

        
        while left < right:
        
            left_height = height[left]
            right_height = height[right]   
            current_area = min(left_height,right_height) * (right - left)
            max_area = max(max_area,current_area)
            
            if right_height < left_height:
                right -= 1
            
            else: 
                left +=1 
        
        
        return max_area
        
        
        
        
# Test Cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea( height = [1,8,6,2,5,4,8,3,7] ))
    print(solution.maxArea( height = [1,1] ))

# Time Complexity: O(n)
# Space Complexity: O(1)