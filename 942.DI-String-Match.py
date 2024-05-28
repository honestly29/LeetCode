class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        perm = []
        i = 0
        d = n

        for j in range(n):

            if s[j] == 'I':
                perm.append(i)
                i+=1
            else:
                perm.append(d)
                d -= 1
            
        if s[-1] == "I":
            perm.append(i)
        else:
            perm.append(d)

        return perm