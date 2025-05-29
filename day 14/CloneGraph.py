
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def __init__(self):
        self.mp = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return None
        if node in self.mp : return self.mp[node]

        copyNode = Node(node.val)
        self.mp[node] = copyNode

        for x in node.neighbors: 
            copyNode.neighbors.append(self.cloneGraph(x))

        
        return copyNode

        