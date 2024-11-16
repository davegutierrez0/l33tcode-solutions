from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Start with two pointers at ends of the array
        len_height = len(height)
        
        water_store = 0

        left = 0
        right = len_height - 1
        left_height_max = 0
        right_height_max = 0
        
        while left < right:
            
            if height[left] < height[right]:
                if height[left] >= left_height_max:
                    left_height_max = height[left]
                else:
                    water_store += left_height_max - height[left]
                left += 1      
                
            
            else:
                if height[right] >= right_height_max:
                    right_height_max = height[right]
                
                else: 
                    water_store += right_height_max - height[right]
                right -= 1
                
                
                
        # print(water_store)
            
            
        return water_store
            
        
        
                
        # while left < right:
        
        #     left_height = height[left]
        #     right_height = height[right]   
        #     current_area = min(left_height,right_height) * (right - left)
        #     max_area = max(max_area,current_area)
            
        #     if right_height < left_height:
        #         right -= 1
            
        #     else: 
        #         left +=1 
        
        
        return total_area
        
        
        
        
# Test Cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap( height = [0,1,0,2,1,0,1,3,2,1,2,1] ))
    print(solution.trap( height = [4,2,0,3,2,5] ))

# Time Complexity: O(n)
# Space Complexity: O(1)