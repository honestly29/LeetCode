class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        import math

        count = 0
        new_lst = []

        for query in queries:

            count = 0
            for point in points:

                point_cord = [point[0], point[1]]
                circle_cord = [query[0], query[1]]
                radius = query[2]

                if math.dist(point_cord, circle_cord) <= radius:
                    count += 1
                
            new_lst.append(count)


        return(new_lst)