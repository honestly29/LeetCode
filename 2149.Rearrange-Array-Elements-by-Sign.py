class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        pos_arr = []
        neg_arr = []

        for num in nums:
            if num >= 0:
                pos_arr.append(num)
            else:
                neg_arr.append(num)

        for i in range(len(pos_arr)):
            ans.append(pos_arr[i])
            ans.append(neg_arr[i])     

        return(ans)