#Running sum of 1D array.

nums = [3,1,8,2,10,5]
runningSum = []
sum = 0
for i in nums:
    sum += i
    runningSum.append(sum)
    
print(runningSum)

