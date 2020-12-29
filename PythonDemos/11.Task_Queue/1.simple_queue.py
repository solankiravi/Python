import queue
#Queue - FIFO
q = queue.Queue()
#Append item in queue
q.put(5)
q.put(89)
#Return item from queue
print(q.get())
#Check whether Queue is empty
print(q.empty())

q.put(16)
while not q.empty():
    print(q.get())