class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        

        ans = []

        for string in words:

            for word in string.split(separator):

                if len(word) > 0:

                    ans.append(word)

        return(ans)