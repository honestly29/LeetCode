class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        
        num_devices = []
        total = 0

        for row in bank:
            
            count = row.count("1")

            if count > 0:

                num_devices.append(count)


        for i in range(len(num_devices)-1):

            total += num_devices[i] * num_devices[i+1]


        return(total)