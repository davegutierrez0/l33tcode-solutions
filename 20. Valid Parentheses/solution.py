class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        i = 0
        pairsDict = {'(':')','[':']','{':'}'}
        sStack = []
        
        while i < len(s):
            
            if s[i] in pairsDict.keys():
                sStack.append(s[i])
            
            elif s[i] in pairsDict.values(): 

                try:
                    if pairsDict[sStack.pop()] != s[i]:
                        return False
                    
                except IndexError as e:
                    return False        


            
            
            i += 1
            
        return True if len(sStack) == 0 else False 

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(s = "]"))
    print(solution.isValid(s = "()"))
    print(solution.isValid(s = "()[]{}"))
    print(solution.isValid(s = "(]"))
    print(solution.isValid(s = "([])"))

    
# Time Complexity O(n)
# Space Complexity O(n)