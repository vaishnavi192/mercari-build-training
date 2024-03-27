class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        countRemoved = 0
        lastNonOverlappingEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < lastNonOverlappingEnd:  
                countRemoved += 1
            else:
                lastNonOverlappingEnd = end  
        
        return countRemoved