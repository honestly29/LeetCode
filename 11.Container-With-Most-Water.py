class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)  
        i, j = 0, n-1 
        area = 0

        while n > 0:

            new_area = (n-1) * min(height[i], height[j])

            if new_area > area:
                area = new_area
            
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

            n -= 1

        return(area)