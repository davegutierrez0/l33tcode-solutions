from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        
        
        while i < len(nums) - 1:
            # print("i:",i)   
            # print("count: ",nums.count(nums[i]))
            
            if nums[i] in nums[i + 1:i + 2 + k]:
                for j in range(i + 1,i + 2 + k):
                    
                    # print("j:",j)
                    if j < len(nums) and nums[i]== nums[j] and (abs(i - j) <= k):
                        return True
        
            i += 1

            
        return False
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    print(solution.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    print(solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

    
