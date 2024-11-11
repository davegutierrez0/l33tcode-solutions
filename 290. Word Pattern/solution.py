class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        word_hash_map = {}
        mapped_words = set()
        s_list = s.split()
        
        for idx in range(len(pattern)):
            if pattern[idx] in word_hash_map:
                if word_hash_map[pattern[idx]] != s_list[idx]:
                    return False
            
            elif idx < len(s_list):
                if s_list[idx] in mapped_words:
                    return False
                word_hash_map[pattern[idx]] = s_list[idx]
                mapped_words.add(s_list[idx])
                
            
        print(word_hash_map)

        return True if len(pattern) == len(s_list) else False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern(pattern = "abba", s = "dog cat cat dog"))
    print(solution.wordPattern(pattern = "abba", s = "dog cat cat fish"))
    print(solution.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
    print(solution.wordPattern(pattern = "aaa", s = "aa aa aa aa"))



# Time Complexity: O(m+n)
# Space Complexity: O(m+n)