# Insert Element at beginning: O(1)
# Delete Element at beginning: O(1)
# Insert/Delete Element at end: O(n)
# Linked list traversal: O(n)
# Accessing element by value: O(n)
# llist in python implements linked list
# Use Array for traversing and indexing (Read operations)and use Linked List for insertion and deletion (Write Operations)
class Node:
    def __init__(self, data= None, next=None): # next = None, here None is the default value
        self.data = data # the data in __init__ and data in self.data are not same (names need not be same)
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None # creates an empty linked list.
        # The first node of the linked list is called the head node. It is the starting point of a linked list.
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # creating an object of Node (creating a new instance of the class node)
        # the next element while inserting in beginning would be the head node
        self.head = node
    
    def insert_at_end(self, data): # same as appned in list
        if self.head is None: # handling the case when there is no element, hence beginning and end is same
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next: # will continue till it rached the end of the list
            itr = itr.next
        itr.next = Node(data) # here next will be None
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length(): # using a function within the same class
            raise Exception("Invalid Index")
        if index ==0:
            self.insert_at_beginning(data) # using a function within the same class
            return
        itr = self.head
        count = 0
        while itr: # if we want to insert at index 2, then we'll have to stop at 1
            if count == index-1:
                node = Node(data, itr.next) # node's next is itr.next
                itr.next = node
                break
            itr = itr.next
            count+=1
        
    def delete_from_left(self):
        self.head = self.head.next
        
    def delete_from_right(self): # works same as pop in list (array)
        itr = self.head
        count = 0
        while itr:
            if count == self.get_length()-2:
                itr.next = None
                break
            itr = itr.next
            count+=1
            
    def delete_at(self, index): # delete by index
        itr= self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            
    def delete_by_value(self, val):
        itr = self.head
        count=0
        while itr.next: # here we use itr.next because we want to stop one before the index of the value that needs to be deleted
            if itr.next.data == val:
                itr.next = itr.next.next
                break
            count+=1
            itr= itr.next
            
    def traverse(self):
        itr = self.head
        result = ""
        while itr:
            result = result+str(itr.data)
            itr=itr.next
        return result
            
    def search_by_value(self, value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                return index
            index+=1
            itr = itr.next
        return "Value not in Linked List"
    
    def search_by_index(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Index out of bound")
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr.data
            count+=1
            itr = itr.next
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_values_reverse(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_beginning(data)
        
    def printf(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head # bascially creating the head node and using it as a pointer
        llstr = "" # linked list string
        while itr:
            suffix =''
            if itr.next:
                suffix='->'
            llstr+=str(itr.data) + suffix
            itr = itr.next
        print(llstr)
        
    def get_length(self): # to get the length of linked list
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count
        
    
root = LinkedList()
root.insert_at_beginning(5)
root.insert_at_beginning(10)
root.insert_at_beginning(19)
root.printf()
root.insert_at_end(99)
root.printf()
root.insert_at(2, 87)
root.printf()
print(root.search_by_value(5))
root.delete_from_left()
root.printf()
root.delete_from_right()
root.printf()
root.insert_at_beginning(198)
root.insert_at_beginning(188)
root.printf()
print(root.search_by_index(2))
root.delete_at(2)
root.printf()
root.delete_by_value(198)
root.printf()

# root.traverse()

# new linked list

ll =LinkedList()
ll.insert_values(["banana", "mango", "grapes", "oranges"])
ll.printf()
ll.traverse()
# ll.insert_values_reverse(["apple", "banana", "oranges"])
# ll.printf()

ll.delete_by_value("mango")
ll.printf()


#print(root.get_length())