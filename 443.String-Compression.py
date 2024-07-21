class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 1

        while j < n:

            if nums[i] != 0 and nums[j] != 0:
                i+=1
            
            if nums[i] == 0 and nums[j] != 0:

                nums[i], nums[j] = nums[j], nums[i]
                i+=1

            j+= 1
