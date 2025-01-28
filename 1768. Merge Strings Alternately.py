class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)


# Improved 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        result = []
        
        for i in range(min_len):
            result += [word1[i], word2[i]]
        
        result.append(word1[min_len:])
        result.append(word2[min_len:])
        return "".join(result)
        
        
