class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0

        for i in range(low, high+1):

            str_num = str(i)
            l = len(str_num)
            
            if l % 2 == 0:

                left = sum([int(i) for i in str_num[:l//2]])
                right = sum([int(i) for i in str_num[l//2:]])
                
                if left == right:
                    count += 1

        return(count)