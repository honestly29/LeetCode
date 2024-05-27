class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        new_list = []

        for nums in rectangles:

            if nums[0] < nums[1]:

                new_list.append(nums[0])

            else:

                new_list.append(nums[1])


        return(new_list.count(max(new_list)))