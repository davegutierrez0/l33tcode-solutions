class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        result = [] 
        
        n = len(digits)
        
        i = n-1 

        addMore = False 
        
        while i >= 0:
            digit = digits[i]    
            
            # Regular add one case
            if i == n - 1 and digit < 9:
                result.insert(0,digit+1)
                addMore = False 
                
            # Trailing nine add one case
            elif i == n - 1 and digit == 9:
                result.insert(0,0)
                

                # Repeating 9 sub-case    
                if digits[i-1] == 9:
                    while i >0 and digits[i-1] == 9:
                        result.insert(0,0)
                        i -= 1

                # Leading 9 sub-case
                if i == 0 and digits[i] == 9:
                    result.insert(0,1)
                    
                # Non-leading 9 sub-case
                if i> 0 and digits[i-1] < 9:
                    digits[i-1] +=1
            
            # Default case 
            else:
                result.insert(0,digit)

            i -= 1
                

    
        return result
    

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne(digits = [1,2,3]))
    print(solution.plusOne(digits = [4,3,2,1]))
    print(solution.plusOne(digits = [9]))
    print(solution.plusOne(digits = [9,9,9]))
    print(solution.plusOne(digits = [9,9]))
    print(solution.plusOne(digits = [8,9,9,9]))
    
