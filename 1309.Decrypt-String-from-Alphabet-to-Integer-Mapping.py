class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        code_list = []
        s_rev = s[::-1]
        i=0

        while i <= len(s)-1:
            if s_rev[i] == '#':
                code_list.append(s_rev[i+1]+s_rev[i+2])
                i+=3
            else:
                code_list.append(s_rev[i])
                i+=1
            

        code_list.reverse()


        for code in code_list:
            ans += (chr(int(code[::-1])+96))

        return(ans)