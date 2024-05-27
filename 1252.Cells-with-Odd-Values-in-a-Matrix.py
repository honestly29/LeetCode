class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0]*m
        columns = [0]*n
        count = 0

        for i,j in indices:
            rows[i] += 1
            columns[j] += 1

        for i in rows:
            for j in columns:
                if (i+j) % 2 == 1:
                    count += 1

        return(count)