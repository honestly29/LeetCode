class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid[0])
        m = len(grid)

        diff = [[0 for _ in range(n)] for _ in range(m)]

        row_ones = []
        col_ones = []

        for i in range(m):
            row_ones.append(grid[i].count(1))


        for i in range(n):
            column = [row[i] for row in grid]
            col_ones.append(column.count(1))
            

        for i in range(m):
            for j in range(n):
                diff[i][j] = (row_ones[i] + col_ones[j] - (m - row_ones[i]) - (n - col_ones[j]))

        return(diff)