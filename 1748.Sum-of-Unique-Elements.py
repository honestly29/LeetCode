class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        count = 0

        for num in nums:
            if nums.count(num) == 1:
                count += num

        return(count)