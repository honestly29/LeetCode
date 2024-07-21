class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        i, j = 0, n-1
        count = 0
        nums.sort()

        while j > i:

            if nums[i] + nums[j] == k:
                count += 1
                i+=1
                j-=1

            elif nums[i] + nums[j] < k:
                i+=1

            else:
                j-=1

        return(count)