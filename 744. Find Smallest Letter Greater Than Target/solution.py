class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        target_number = ord(target) + 1

        for letter in letters:
            if ord(letter) + 1 > target_number:
                return letter

        return letters[0]