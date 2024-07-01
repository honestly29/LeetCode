class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        my_dict = {}
        ans = []

        if len(items1) > len(items2):
            big = items1
            small = items2
        else:
            big = items2
            small = items1

        for i in range(len(big)):
            my_dict[big[i][0]] = big[i][1]


        for i in range(len(small)):
            if small[i][0] in my_dict.keys():
                my_dict[small[i][0]] += small[i][1]

            else:
                my_dict[small[i][0]] = small[i][1]


        for key, value in my_dict.items():
            ans.append([key, value])

        ans.sort()

        return ans