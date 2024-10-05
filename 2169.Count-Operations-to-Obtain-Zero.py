class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sumLeft = 0
        sumRight = sum(nums)

        for idx, ele in enumerate(nums):

            sumRight -= ele

            if sumLeft == sumRight:

                return idx

            sumLeft += ele

        return -1

   