class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        romanValues = {
              "I" : 1,
              "V" : 5,
              "X" : 10,
              "L" : 50,
              "C" : 100,
              "D" : 500,
              "M" : 1000 
        }

        for i in range(len(s)-1,-1,-1):
            currentValue = romanValues[s[i]]
            previousValue = romanValues[s[i + 1]] if i <len(s)-1  else 0

            if currentValue >= previousValue:
                total += currentValue
            else:
                total -= currentValue

                                
        return total

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVII"))
    print(solution.romanToInt("MCMXCIV"))
    
