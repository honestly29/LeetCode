class Solution:
    def countBits(self, n: int) -> list[int]:
        
        ans = [str(bin(i)).count('1') for i in range(n+1)]

        return ans