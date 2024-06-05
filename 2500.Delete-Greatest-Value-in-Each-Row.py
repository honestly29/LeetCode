class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        count = 0
        new_lst = []

        for i in range(len(grid)):  
            new_lst.append(sorted(grid[i]))


        for i in range(len(grid[0])):
            temp = 0

            for j in range(len(grid)):
                
                if new_lst[j][i] > temp:
                    temp = new_lst[j][i]

            count += temp


        return(count)