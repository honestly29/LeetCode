class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        count_one = 0
        idx = 0

        for i in range(len(mat)):

            ones = sum(mat[i])

            if ones > count_one:

                count_one = ones
                idx = i

        return [idx, count_one]
