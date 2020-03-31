nums = [2, 7, 11, 15]
target = 9
loop = 0
for i in range(len(nums) -1 ):
    if loop == 0:
            for j in range(len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    if i == j:
                        pass
                    else:
                        print(i,j)
                        loop = 1
