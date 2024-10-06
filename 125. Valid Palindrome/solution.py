import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFiltered = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        # print("Alphanumeric string: ",sFiltered)
        
        if sFiltered == "":
            return True
    
        # Python's [::-1] shorthand reverses the string or list
        return True if sFiltered[::-1] in sFiltered else False
        
                 
        
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s = "race a car"))
    print(solution.isPalindrome(s = "racecar"))
    
