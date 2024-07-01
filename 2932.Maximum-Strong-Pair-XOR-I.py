class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(len(nums)):

            for j in range(i, len(nums)):

                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):

                    curr = nums[i] ^ nums[j]

                    if curr > res:

                        res = curr

        return(res)