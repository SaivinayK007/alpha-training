from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.arr = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not  in self.arr :
            return -1
        self.arr.move_to_end(key)
        return self.arr[key]


    def put(self, key: int, value: int) -> None:
        if key in self.arr:
            self.arr.move_to_end(key)
        self.arr[key] = value

        if len(self.arr) > self.size :
            self.arr.popitem(last = False)
        


    

"""
   Use Ordered Dictionary or Dictionary in Python

"""