class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        result = 0 
        
        for num in nums:
            result ^= num
        
        return result
    

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([2,2,1]))
    
