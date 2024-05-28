class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []

        for i in range(left, right+1):

            num = str(i)

            if '0' not in num:

                count = 0
                for j in num:
                    if int(num) % int(j) == 0:
                        count += 1


                if count == len(num):
                    ans.append(int(num))

        return(ans)