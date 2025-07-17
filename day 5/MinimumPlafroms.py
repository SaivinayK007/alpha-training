#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        '''
         max overlap in schedule
        '''
        arr.sort()
        dep.sort()
        n = len(arr)
        
        i = j = pReq = mReq = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                pReq += 1
                mReq = max(mReq , pReq)
                i+= 1
            else :
                pReq -=1
                j +=1
        return mReq
    
'''

  Time Complexity: O(n log n)

'''
https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/