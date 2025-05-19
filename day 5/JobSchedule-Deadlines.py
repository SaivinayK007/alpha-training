class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        jobs = dict()
            
        for i in range(len(profit)):
            jobs[profit[i]] = deadline[i]


        myKeys = list(jobs.keys())
        myKeys.sort(reverse=True)

        jobs = {i : jobs[i] for i in myKeys}
        print(jobs)

        
        slots = [0] * (max(deadline) + 1)
        count = 0
        
        # for ind , ele  in enumerate(profit):
        #     temp = deadline[ind]
            
        #     if count == max(deadline): break
            
        #     while temp >= 1:
        #         if slots[temp] == 0:
        #             slots[temp] = ele
        #             count +=1
        #             break
                
        #         temp -=1
                    
        # return [count , sum(slots)]
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
profit = [10 , 20 , 30 , 40]
deadline = [1,4,1,1]

obj = Solution()
ans = obj.jobSequencing(deadline, profit)

print(ans)
# } Driver Code Ends