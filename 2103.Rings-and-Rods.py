class Solution:
    def countPoints(self, rings: str) -> int:
        
        count = 0
        new_dict = {}

        for char in rings:
            if char.isdigit():
                new_dict[char] = []


        for i in range(1, len(rings), 2):
            new_dict[rings[i]].append(rings[i-1])


        for value in new_dict.values():
            if len(set(value)) == 3:
                count += 1

        return(count)