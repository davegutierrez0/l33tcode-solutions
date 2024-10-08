from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        elif target < nums[0]:
            return 0

        elif target > nums[len(nums)-1]:
            return len(nums)

        else: 
            middleIndex = (len(nums)-1) // 2
            # print("middleIndex:", middleIndex)


            if nums[middleIndex -1] < target < nums[middleIndex]:
                return middleIndex 
            
            elif target > nums[middleIndex]:
                endIndex = len(nums) - 1
                

                while target < nums[endIndex]:
                    endIndex -= 1
                    
                return endIndex + 1
            
            elif target < nums[middleIndex]:
                beginningIndex = 0
                                                    
                while target < nums[middleIndex]:
                    middleIndex -= 1


                return middleIndex + 1
                
                        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert(nums = [1,3,5,6], target = 5))
    print(solution.searchInsert(nums = [1,3,5,6], target = 2))
    print(solution.searchInsert(nums = [1,3,5,6], target = 7))
    print(solution.searchInsert(nums = [1,3,5], target = 4))
    
    
