class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        

        result = [] 
        
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        
        return result
    

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
    print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    
