from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        
        i = 0
        
        while i < len(nums):
            start = nums[i]
            interval = str(start)
            
            while i < len(nums) - 1 and nums[i+1] - 1 == nums[i]:
                i += 1
            
            if nums[i] == start:
                ranges.append(interval)
            else:
                ranges.append(interval + ("->" + str(nums[i])))
            
            i += 1

        return ranges

# Test Cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges( nums = [0,1,2,4,5,7] ))
    print(solution.summaryRanges( nums = [0,2,3,4,6,8,9] ))

# Time Complexity: O(n)
# Space Complexity: O(1)