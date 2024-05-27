class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
        count_a = 0
        count_b = 0

        a, b = s[:len(s)//2], s[len(s)//2:]

        for letter in a:
            if letter in vowels:
                count_a += 1

        for letter in b: 
            if letter in vowels:
                count_b += 1

        return(count_a == count_b)