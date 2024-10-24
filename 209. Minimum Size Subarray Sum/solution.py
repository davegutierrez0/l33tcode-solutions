from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        min_length = math.inf 

        start, end, sum_nums = 0, 0, 0
        
        while end < len(nums):
            
            sum_nums += nums[end]

            while sum_nums >= target:
                min_length = min(min_length, end - start + 1)
                sum_nums -= nums[start]
                start += 1
            
            end += 1
            


        return 0 if min_length > len(nums) else min_length


# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(target = 15, nums = [1,2,3,4,5]))
    print(solution.minSubArrayLen(target = 213, nums = [12,28,83,4,25,26,25,2,25,25,25,12]))
    print(solution.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
    print(solution.minSubArrayLen(target = 4, nums = [1,4,4]))
    print(solution.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))

# Time Complexity O(n)
# Space Complexity O(1)
