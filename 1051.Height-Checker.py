class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        arranged = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != arranged[i]:
                count += 1

        return(count)