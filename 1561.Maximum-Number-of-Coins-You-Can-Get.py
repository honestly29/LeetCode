class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        total = 0

        piles.sort()

        for i in range(int(n/3), n, 2):

            total += piles[i]

        return(total)