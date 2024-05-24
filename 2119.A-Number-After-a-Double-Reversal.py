class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        str_num = str(num)

        if len(str_num) > 1 and str_num[-1] == '0':
            return False
        
        return True