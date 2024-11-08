class Solution:
    def intToRoman(self, num: int) -> str:
        
        result = ''
        
        romanValues = {
        1000:    'M',
            900:    'CM',
            500:    'D',
            400:    'CD',
            100:    'C',
            90:    'XC',
            50:    'L',
            40:    'XL',
            10:    'X',
            9:    'IX',
            5:    'V',
            4:    'IV',
            1:    'I'
        }

        for key in romanValues:
            
            while key <= num:
                num -= key
                result += romanValues[key]
            
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(num = 3749))
    print(solution.intToRoman(num = 58))
    print(solution.intToRoman(num = 1994))



# Time Complexity: O(n)
# Space Complexity: O(1)