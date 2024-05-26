class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()

        for i in range(0, len(nums)-1, 2):

            ans += (min(nums[i], nums[i+1]))

        return(ans)