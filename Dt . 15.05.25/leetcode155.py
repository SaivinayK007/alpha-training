class MinStack:

    def __init__(self):
        self.arr = list()
        
    def push(self, val: int) -> None:

        if len(self.arr) == 0:
            self.arr.append((val , val))
        else:
            if val > self.arr[-1][1]:
                self.arr.append((val , self.arr[-1][1]))
            else:
                self.arr.append((val , val))
    
    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        