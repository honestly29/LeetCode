class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len_word1 = len(word1)
        len_word2 = len(word2)

        N = min(len_word1, len_word2)

        new_word = ""

        for i in range(N):
            new_word += word1[i]
            new_word += word2[i]


        if len_word1 > len_word2:
            new_word += word1[N:]
        else:
            new_word += word2[N:]


        return(new_word)