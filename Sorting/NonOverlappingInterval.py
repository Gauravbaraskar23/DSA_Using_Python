# 435. Non-overlapping Intervals
# Given a collection of intervals, 
# find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    
    prev = 0
    count = 1
    
    for i in range(1, n):
        if intervals[i][0] >= intervals[prev][1]:
            count += 1
            prev = i
            
    return n - count
    

print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))