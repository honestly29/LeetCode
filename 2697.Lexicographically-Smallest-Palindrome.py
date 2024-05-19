class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        import math

        N = len(s)
        s_lst = list(s)

        for i in range(math.floor(N/2)):
            
            if s[i] != s[N-i-1]:

                if s[i] > s[N-i-1]:
                
                    s_lst[i] = s_lst[N-i-1]

                else:
                
                    s_lst[N-i-1] = s_lst[i]

                

        return ("".join(s_lst))