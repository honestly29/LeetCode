class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0

        for row in grid:
            for num in sorted(row):

                if num >= 0:
                    break

                count += 1

        return(count)