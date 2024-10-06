
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True 
            
        sPointer = 0
        
        for char in t:
            if char == s[sPointer]:
                sPointer +=1
                
                if sPointer == len(s):
                    return True
                
        return False


# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence(s = "abc", t = "ahbgdc"))
    print(solution.isSubsequence(s = "axc", t = "ahbgdc"))
    print(solution.isSubsequence(s = "", t = "ahbgdc"))
    print(solution.isSubsequence(s = "el", t = ""))
