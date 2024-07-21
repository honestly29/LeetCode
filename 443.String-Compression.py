class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        idx = 0
        i = 0

        while i < n:
            j = i
            
            while j < n and chars[j] == chars[i]:
                j+=1

            chars[idx] = chars[i]
            idx += 1

            if j - i > 1:
                for val in str(j-i):
                    
                    chars[idx] = val
                    idx += 1

            i = j

        return(idx)