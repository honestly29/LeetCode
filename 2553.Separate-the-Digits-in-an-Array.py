class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        new_str = ""
        ans = []

        for num in nums:
            new_str += str(num)

        for num in new_str:
            ans.append(int(num))

        return(ans)