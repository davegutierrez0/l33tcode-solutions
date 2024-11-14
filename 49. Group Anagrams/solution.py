from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                
        hash_set_dictionary = {}
                
        for word in strs:
            word_sorted = "".join(sorted(word))
            
            if hash_set_dictionary.get(word_sorted) is None:
                hash_set_dictionary[word_sorted] =  [word]

            else:
                hash_set_dictionary[word_sorted].append(word)
                
        
        return list(hash_set_dictionary.values())


    
        
        
# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(strs = ["ddddddddddg","dgggggggggg"]))    
    print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))    
    print(solution.groupAnagrams( strs = [""]))
    print(solution.groupAnagrams(strs = ["a"]))
    
# Time Complexity: O(n*k*log(k))
# Space Complexity: O(n*k)