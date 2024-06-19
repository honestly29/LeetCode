class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return -1
            
        max_num = max(nums)
        min_num = min(nums)

        for num in nums:

            if num != max_num and num != min_num:
                return(num)
                
        return -1