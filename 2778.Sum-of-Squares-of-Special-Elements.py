class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        count = 0
        N = len(nums)

        for i in range(0, N):

            if N % (i+1) == 0:

                count += nums[i]**2

        return(count)