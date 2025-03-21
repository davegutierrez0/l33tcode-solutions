class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i] > subsequence[-1]:
                subsequence.append(nums[i])
            else:
                j = 0
                while nums[i] > subsequence[j]:
                    j += 1
                subsequence[j] = nums[i]
                        

        return len(subsequence)

# Time Complexity: O(N^2)
# Space Complexity: O(N)