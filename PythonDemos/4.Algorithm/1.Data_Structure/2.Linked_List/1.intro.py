class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        
        itr.next=Node(data,None)

    def append_values(self,data_list):
        # self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count=0
        itr=self.head
        while itr:
            count +=1
            if(count == index -1):
                itr.next = itr.next.next
                return
            itr=itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head.data== data:
            self.head = self.head.next

        itr= self.head
        while itr.next:
            if itr.next.data == data:
                self.head=self.head.next
                break
            itr = itr.next
    
    def insert_after_values(self,data_after,data_to_insert):
        if self.head is None:
            return
        
        if self.head.data== data_to_insert:
            self.head.next=Node(data_to_insert,self.head.next)
            return
        itr= self.head
        while itr:
            if(itr.data == data_after):
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr= self.head
        while itr:
            count += 1
            if count == index - 1:
                node=Node(data,itr.next)
                itr.next=node
                return
            itr= itr.next

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count += 1
            itr= itr.next
        return count 

    def print(self):
        if(self.head) is None:
            print("Linked List is empty")
            return
        itr=self.head
        listr=''
        while(itr):
            listr += str(itr.data) + '=====>'
            itr=itr.next
        print(listr)

if __name__=='__main__':
    l1=LinkedList()
    l1.insert_at_begining(5)
    l1.insert_at_begining(89)
    l1.insert_at_end(79)
    l1.append_values(['a','b','c'])
    l1.print()
    print(l1.get_length())
    l1.remove_at(4)
    l1.insert_at(4,'e')
    l1.print()