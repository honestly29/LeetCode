class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        my_dict = {}
        ans = []

        for i in range(len(names)):
            my_dict[heights[i]] = names[i]


        heights.sort(reverse=True)

        for num in heights:
            ans.append(my_dict[num])

        return(ans)