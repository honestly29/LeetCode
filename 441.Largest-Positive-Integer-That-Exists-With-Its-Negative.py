class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        i = 0
        j = len(nums)-1

        while i != j:
            if nums[i] - (nums[i] * 2) == nums[j]:
                return(nums[i])
            
            elif nums[i] > abs(nums[j]):
                i += 1

            else:
                j -= 1

        return -1