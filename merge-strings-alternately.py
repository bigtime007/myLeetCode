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


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Pointer Solution
        pointer1, pointer2 = 0, 0
        result = []
        
        # Iterate until one of the strings is exhausted
        while pointer1 < len(word1) and pointer2 < len(word2):
            result.append(word1[pointer1])
            result.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1
        
        # Correctly append the remaining characters of the longer string
        if pointer1 < len(word1):
            result.append(word1[pointer1:])
        if pointer2 < len(word2):
            result.append(word2[pointer2:])
        
        return ''.join(result)
