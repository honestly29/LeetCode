class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        new_lst = []
        
        for char in set(s):
            new_lst.append(s.count(char))

        return(all(x == new_lst[0] for x in new_lst))