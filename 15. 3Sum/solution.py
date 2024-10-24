from typing import List
import itertools

class Solution:
    def threeSum(self, nums: List[int]):
        
        nums.sort()
        
        answer_set = set()
        
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break
            
            
            first_number = nums[i]
            left, right = i+1, len(nums) -1
        
            while left < right: 
                second_number = nums[left]
                third_number = nums[right]
                total = first_number + second_number + third_number
                
                
                if total == 0:
                    answer_set.add((first_number,second_number,third_number))
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                    
                else:
                    right -= 1
                

        return [list(answer) for answer in answer_set]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums = [3,0,-2,-1,1,2]))    
    print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))    
    print(solution.threeSum(nums = [0,1,1]))
    print(solution.threeSum(nums =[0,0,0]))
    
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)