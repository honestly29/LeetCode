class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        ans=[]
        dicc={}

        for j in range(len(score)):
            dicc[score[j][k]]=score[j]

        for j in sorted(dicc.keys(),reverse=True):
            ans.append(dicc[j])
        
        return ans