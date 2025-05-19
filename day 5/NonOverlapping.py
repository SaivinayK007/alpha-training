class Solution:
    def eraseOverlapIntervals(intervals) -> int:
        
        def revSort(i):
            return i[1]
        intervals.sort(key = revSort)

        count = 1
        i = 0 
        for j in range(1 , len(intervals)):
            if intervals[j][0] >= intervals[i][1]  and intervals[j][1] >= intervals[i][1]:
                count +=1
                i = j #updates to index in list which satifies valid meeting j 
        
        return len(intervals) - count
Sol = Solution()
Sol.eraseOverlapIntervals([])


"""
Time Complexity :
 O(nlogn) + O(n) = O(NlogN)

"""
            
        