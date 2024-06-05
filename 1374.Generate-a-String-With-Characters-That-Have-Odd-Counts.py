class Solution:
    def generateTheString(self, n: int) -> str:
        
        if n % 2 == 1:
            new_str = "a"*n
        else:
            new_str = "a"*(n-1)+"b"

        return(new_str)