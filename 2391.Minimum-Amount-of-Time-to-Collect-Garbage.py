class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        time = 0

        for house in garbage:
            time += len(house)

        check_lst = []

        for i in range(len(garbage)-1, -1, -1):

            for char in set(garbage[i]):

                if char not in check_lst:

                    time += sum(travel[:i])
                    check_lst.append(char)

        return(time)