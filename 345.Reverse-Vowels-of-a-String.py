
# two pointer optimal
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels=set('AEIOUaeiou')
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s
    
# unoptimal solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "aeiouAEIOU"
        vowels_in_s = ""
        ans = ""
        j = 0

        for i in range(len(s)-1, -1, -1):
            
            if s[i] in vowels:

                vowels_in_s += s[i]


        for i in range(len(s)):

            if s[i] not in vowels:

                ans += s[i]

            else:
                ans += vowels_in_s[j]
                j += 1


        return(ans) 