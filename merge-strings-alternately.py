class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Simple Loop
        result = []
        minLength = min(len(word1), len(word2))
    
        # Merge the strings alternately
        for i in range(minLength):
            result.append(word1[i])
            result.append(word2[i])
    
        # Correctly append the remaining part of the longer string
        result.append(word1[minLength:])
        result.append(word2[minLength:])
    
        return ''.join(result)
