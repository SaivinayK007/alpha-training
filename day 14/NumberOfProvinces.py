class Solution:
    def dfs(self,s,adj,vis):
        vis[s] = 1
        for i in range(len(adj)):
            if adj[s][i] and vis[i] == 0 : self.dfs(i,adj,vis)



    def findCircleNum(self, adj)  -> int:
        n = len(adj)
        count = 0
        vis = [0] * n


        for i in range(n):
            if vis[i] == 0 : self.dfs(i,adj,vis);count+=1
        
        return count
        