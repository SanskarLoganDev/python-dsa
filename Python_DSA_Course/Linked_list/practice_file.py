class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node
        
    def insert_at_index(self, index, data):
        itr = self.head
        count=0
        while itr:
            if count==index-1:
                node = Node(data, itr.next)
                itr.next = node
            count+=1
            itr = itr.next
            
    def delete_at_beginning(self):
        itr = self.head
        self.head = itr.next
        
    def delete_at_end(self):
        itr = self.head
        index = 0
        while itr:
            if index == self.get_length()-2:
                itr.next = None
                break
            itr = itr.next
            index+=1
            
    def delete_at_index(self, index):
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            
    def traverse(self):
        itr = self.head
        result = ""
        while itr:
            result+=str(itr.data)+" "
            itr = itr.next
        return result
    
    def search_by_value(self, value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index+=1
        return "Value not in linked list"
    
    def search_by_index(self,index):
        if index<0 or index>=self.get_length():
            return "Index out of bounds"
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr.data
            itr=itr.next
            count+=1
        
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def printf(self):
        if self.head is None:
            return "Empty Linked List"
        llstr = ""
        itr = self.head
        while itr:
            suffix = ""
            if itr.next:
                suffix = '->'
            llstr+=str(itr.data)+suffix
            itr=itr.next
        return llstr
    
    def head_val(self):
        return self.head.data
    
l = LinkedList()
l.insert_at_beginning(40)
l.insert_at_beginning(36)
l.insert_at_end(78)
l.insert_at_end(722)
l.insert_at_end(29)
print(l.printf())
l.insert_at_index(2,44)
print(l.printf())
l.delete_at_beginning()
print(l.printf())
l.delete_at_end()
print(l.printf())
l.delete_at_index(2)
print(l.printf())
print(l.search_by_value(43))
print(l.search_by_index(2))
print(l.traverse())
print(l.head_val())
