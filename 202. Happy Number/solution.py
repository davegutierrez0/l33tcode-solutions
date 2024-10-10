class Solution:
    def isHappy(self, n: int) -> bool:
        iterations = 0
        nStr = str(n)
        
        while (len(nStr) != 1) or iterations < 10:
            firstPass = False
            nList = [nStr[i:i+1] for i in range(0,len(nStr))]
            # print(nList)
            
            n = 0
            for digit in nList:
                n += int(digit) * int(digit)
            
            nStr = str(n)
            iterations += 1

        # print(n)
        
        
        return True if int(nStr) == 1 else False
        

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(n = 19))
    print(solution.isHappy(n = 2))
    print(solution.isHappy(n = 7))
    print(solution.isHappy(n = 1111111))

    
