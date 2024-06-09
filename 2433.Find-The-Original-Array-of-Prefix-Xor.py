class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ans = [pref[0]]
        xor = 0

        for i in range(1, len(pref)):

            curr = pref[i] ^ pref[i-1]

            ans.append(curr)
        
        return ans