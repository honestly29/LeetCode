class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2, n-1):
            num = n
            digits = []

            while num:
                digits.append(num % i)
                num //= i

            new_str = ''.join(str(x) for x in digits[::-1])

            if new_str != new_str[::-1]:

                return(False)

        return True