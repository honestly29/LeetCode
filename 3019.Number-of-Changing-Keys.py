class Solution:
    def countKeyChanges(self, s: str) -> int:
        s_low = s.lower()
        count = 0

        for i in range(1, len(s)):

            if s_low[i] != s_low[i-1]:

                count += 1

        return(count)
