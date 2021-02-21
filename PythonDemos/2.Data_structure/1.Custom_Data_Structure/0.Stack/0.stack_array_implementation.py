'''
The stack is a linear data structure where elements are arranged sequentially. It follows the mechanism L.I.F.O which means last in first out. 
So, the last element inserted will be removed as the first. 
The operations are:
    Push → inserting an element into the stack
    Pop → deleting an element from the stack
'''

class mystack:
    def __init__(self,max_size=10):
        self.data=[]
        self.max_size = max_size
    
    def length(self):
        return len(self.data)
    
    def is_full(self):
        return len(self.data) == self.max_size
    
    def pop(self):
        if(len(self.data))==0:
            return "underflow"
        return self.data.pop()

    def push(self,element):
        if len(self.data) > self.max_size:
            return "Overflow"
        return self.data.append(element)

obj = mystack()
obj.pop()
obj.push(5)
print(obj.data)
print(obj.length())