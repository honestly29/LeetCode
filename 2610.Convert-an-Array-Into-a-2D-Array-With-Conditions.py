class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        max = 0
        for num in set(nums):
            curr = nums.count(num)
            if curr > max:
                max = curr

        my_dict = [[] for _ in range(max)]

        for num in nums:

            for row in my_dict:

                if num not in row:

                    row.append(num)
                    break

        return(my_dict)