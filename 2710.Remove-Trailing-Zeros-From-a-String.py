class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        count = 0
        N = len(num)

        for i in range(N-1, 0, -1):

            if num[i] == "0":

                count += 1

            else:
                break

        return(num[:N-count])