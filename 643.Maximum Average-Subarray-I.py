class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        new_sum = sum(nums[:k]) 
        max_average = new_sum / k

        for i in range(n-k):

            new_sum = new_sum - nums[i] + nums[i+k]

            max_average = max(max_average, new_sum/k)

        return(max_average)