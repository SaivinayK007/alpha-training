def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q : return True
        if not p or not q : return False 
        return p.val == q.val and self.isSameTree(p.left , q.left) and self.isSameTree(p.right ,q.right)

def visit(self , root):
        self.temp =[]
        if root :
                self.temp.append(root.val)
                self.visit(root.left)
                self.visit(root.right)
        else:
                self.temp.append(None)
        return self.temp
def isSame(self , p , q):
        if not p and not q : return True
        if not p or not q : return False 
        
        self.temp = self.visit(p)
        self.temp1= [self.visit(q)]

        return self.temp == self.temp1
