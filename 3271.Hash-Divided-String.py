class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        n = len(s)
        ans = ''

        for i in range(0, n, k):
            hash_value = 0

            for j in s[i:i+k]:
                hash_value += ord(j) - 97

            hashed_char = hash_value % 26
            ans += chr(hashed_char + 97)

        return(ans)



