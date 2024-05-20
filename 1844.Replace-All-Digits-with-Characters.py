class Solution:
    def replaceDigits(self, s: str) -> str:
        
        list_s = list(s)

        def shift(c, x):
            return chr(ord(c)+int(x))

        for i in range(1, len(s), 2):
            list_s[i] = shift(s[i-1], s[i])
            

        return("".join(list_s))