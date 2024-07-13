nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]


m = len(l)
res = []
#nums.sort()

for i in range(m):

    curr = sorted(nums[l[i]:r[i]+1])
    count = 0

    for j in range(len(curr)-1):

        if curr[j+1] - curr[j] == curr[1] - curr[0]:
            continue

        else:
            res.append(False)
            break
    else:
        res.append(True)
    
print(res)


