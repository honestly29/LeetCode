class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hash = {}

        for num in arr:
            if num not in hash:
                
                hash[num] = 1
            
            else:

                hash[num] += 1

        return(len(hash.values()) == len(set(hash.values())))