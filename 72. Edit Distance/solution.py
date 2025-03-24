class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        memo = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        def minDistanceRecursive(word1, word2, word_1_index, word_2_index):
            # Base Case

            if word_1_index == 0:
                return word_2_index
            
            if word_2_index == 0:
                return word_1_index

            if memo[word_1_index][word_2_index] is not None:
                return memo[word_1_index][word_2_index]

            minimum_edit_distance = 0

            if word1[word_1_index - 1] == word2[word_2_index - 1]:
                minimum_edit_distance = minDistanceRecursive(word1, word2, word_1_index - 1, word_2_index - 1)

            else:
                # Calculate the cost of insert, delete or replace operations
                insert_operation = minDistanceRecursive(word1, word2, word_1_index, word_2_index - 1)
                delete_operation = minDistanceRecursive(word1, word2, word_1_index - 1, word_2_index)
                replace_operation = minDistanceRecursive(word1, word2, word_1_index - 1, word_2_index - 1)

                minimum_edit_distance = min(insert_operation,delete_operation,replace_operation) + 1
            memo[word_1_index][word_2_index] = minimum_edit_distance
            return minimum_edit_distance 

        return minDistanceRecursive(word1,word2,len(word1),len(word2))

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)