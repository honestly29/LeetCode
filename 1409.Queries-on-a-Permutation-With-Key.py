class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        ans = []

        p = [i for i in range(1, m+1)]

        for i in range(len(queries)):

            idx = p.index(queries[i])
            ans.append(idx)
            p.insert(0, p.pop(idx))
            

        return(ans)