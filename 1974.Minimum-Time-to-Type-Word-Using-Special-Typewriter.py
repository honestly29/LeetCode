class Solution:
    def minTimeToType(self, word: str) -> int:
        
        ans = len(word)
        prev = "a"

        for char in word:
            
            val = (ord(char) - ord(prev)) % 26
            ans += min(val, 26-val)
            prev = char

        return(ans)
