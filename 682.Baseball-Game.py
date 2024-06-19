class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []

        for i in range(len(operations)):

            if operations[i] == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))

            elif operations[i] == 'D':
                scores.append(int(scores[-1]) * 2)

            elif operations[i] == 'C':
                del scores[-1]

            else:
                scores.append(int(operations[i]))

        return(sum(scores))