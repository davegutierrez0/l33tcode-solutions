from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        answer = [1] * length_nums

        left_product, right_product = 1, 1
        
        for i in range(length_nums):
            answer[i] = left_product
            left_product *= nums[i]
            
            
        for j in range(length_nums -1, -1, -1):
            answer[j] *= right_product
            right_product *= nums[j]
            
        return answer
    
    
    # Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums = [1,2,3,4]))    
    print(solution.productExceptSelf(nums = [-1,1,0,-3,3]))
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)
    
    
# Old answer that times out due to being O(n^2)    
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#         length_nums = len(nums)

#         for i in range(length_nums):
#             filtered_list = nums[:i] + nums[i + 1:]
#             answer.append(prod(filtered_list))

#         return answer


