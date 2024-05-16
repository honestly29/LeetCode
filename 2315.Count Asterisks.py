class Solution:
    def countAsterisks(self, s: str) -> int:
        
        flag = True

        count = 0

        for char in s:

            if char == '|' and flag:
                flag = False
            else:
                if char == '|' and not flag:
                    flag = True
                
            if char == '*' and flag:
                count += 1

        return (count)
  
print(1)
