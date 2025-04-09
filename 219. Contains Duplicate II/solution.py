from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict and abs(nums_dict[nums[i]] - i) <= k:
                return True

            nums_dict[nums[i]] = i

        return False
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    print(solution.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    print(solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

    
# Time Complexity: O(N)
# Space Complexity: O(N)

# “If I’ve seen this number before, and it’s not too far back, return True.
# Otherwise, update its last-seen location.”