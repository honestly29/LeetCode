class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        curr = 0
        count = 0

        for i in range(len(nums)):

            curr += nums[i]
            
            if curr == 0:
                count += 1

        return(count)