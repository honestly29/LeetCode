class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        curr = 0

        while curr < len(boxes):
            count = 0

            for i in range(len(boxes)):

                if i != curr and boxes[i] == '1':

                    count += abs(i - curr)

            ans.append(count)
            curr += 1

        return(ans)