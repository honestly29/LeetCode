class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        ans = 0

        for num in nums:
            
            num_str = str(num)
            ans += int(max(num_str) * len(num_str))

        return(ans)