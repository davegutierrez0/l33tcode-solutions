from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        i = 0
        
        while i <= len(numbers) - 2:        
            lookingFor = target - numbers[i]
            if lookingFor in numbers[i+1:]:
                return [i+1,numbers[i+1:].index(lookingFor)+i+2]                        
            i += 1
            

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(numbers = [2,7,11,15], target = 9))
    print(solution.twoSum(numbers = [2,3,4], target = 6))
    print(solution.twoSum(numbers = [-1,0], target = -1))
    
