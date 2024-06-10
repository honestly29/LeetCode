class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        my_dict = {}
        res = []

        for num in set(groupSizes):
            my_dict[num] = []


        for i, num in enumerate(groupSizes):
            my_dict[num].append(i)
            

        for key in my_dict:

            if key == len(my_dict[key]):

                res.append(my_dict[key])

            else:

                start = 0
                for i in range(key, len(my_dict[key])+1, key):
                    stop = i

                    res.append(my_dict[key][start:stop])

                    start += key

        return(res)