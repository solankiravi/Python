'''
The queue is a linear data structure where elements are in a sequential manner. 
It follows the F.I.F.O mechanism that means first in first out.

Two ends:
front → points to starting element
rear → points to the last element

There are two operations:
enqueue → inserting an element into the queue. It will be done at the rear.
dequeue → deleting an element from the queue. It will be done at the front.

There are two conditions:
overflow → insertion into a queue that is full
underflow → deletion from the empty queue
'''

class myqueue:
    def __init__(self,max_size=10):
        self.data=[]
        self.max_size=max_size
    
    def length(self):
        return len(self.data)

    def enqueue(self,element):
        if len(self.data) > self.max_size:
            return "Overflow"
        return self.data.append(element)
    
    def dequeue(self):
        if len(self.data) == 0:
            raise Exception("underflow")
        return self.data.pop(0)

obj = myqueue()
obj.enqueue(20)
obj.enqueue(40)
print(obj.data)
obj.dequeue()
print(obj.data)        