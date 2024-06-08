class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        new_list = []

        for i in range(1, len(nums)+1):

            new_list.append(len(set(nums[:i])) - len(set(nums[i:])))


        return(new_list)
