# Question: replace the maximum value of a linked list with a given value. Assume whole numbers and only one maximum value

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        #check empty condition
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr= itr.next
        node = Node(data, None)
        itr.next = node
        
    def insert_at(self, data, index):
        if index<0 or index>self.get_length():
            raise Exception("Index out of bound")
        if index==0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count=0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
            
    def traverse(self):
        itr = self.head
        result = ""
        while itr:
            result = result+str(itr.data)
            itr=itr.next
        return result
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def printf(self):
        if self.head == None:
            print("Empty List")
            return
        itr = self.head
        llstr =""
        while itr:
            suffix = ""
            if itr.next:
                suffix="->"
            llstr+=str(itr.data)+suffix
            itr=itr.next
        return llstr
    
    # PROBLEM 1: find the maximum value in LL and replace it with a given value
    
    def replace_max_efficient(self, value):
        itr =  self.head
        max =itr # take the entire node in max and not just the value
        while itr:
            if itr.data > max.data:
                max = itr
            itr =itr.next
        max.data = value
    
    # PROBLEM 2: sum the values at odd indexes of a LL
    
    def sum_odd_indexes(self):
        itr = self.head
        count=0
        sum = 0
        while itr:
            if count%2 != 0:
                sum+=itr.data
            itr = itr.next
            count+=1
        return sum
    
    # PROBLEM 3: reverse a LL (Very Important)
    
    def reverse(self):
        itr = self.head # current node
        prev_node = None
        while itr:
            next_node = itr.next # storing next in different variable so that the connection does not break and the loop can go forward to the next node
            itr.next = prev_node
            prev_node = itr # first we move the previous node forward and then the current node as
            itr = next_node # equivalent to itr = itr.next that we commonly use
        
        self.head = prev_node
        
    # PROBLEM 4: String mainupulation using the following rules:
    # 1) Replace * or / by a single space
    # 2) Replace consecutive * or / by a single space and convert the next character to upper case
    
    # Assume: no more than two consecutive * or / and a linked list will always wnd with an alphabet    
    
    def string_manipulation(self):
        itr = self.head
        space = " "
        while itr:
            if itr.data == '*' or itr.data == '/':
                itr.data = space
                if itr.next.data == '*' or itr.next.data == '/':
                    itr.next.data=""
                    itr.next.next.data = itr.next.next.data.upper()
            itr = itr.next
                
    # PROBLEM 5: Remove duplicates from a linked list
    def remove_duplicates(self):
        itr = self.head
        while itr and itr.next:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else: # here else is reauired to handle cases where duplicates occur more than twice, directly increasing itr to itr.next will skip comparisons
                itr = itr.next
                
    def remove_duplicates_alt(self):
        itr = self.head
        while itr:
            while itr.next and itr.data == itr.next.data:
                itr.next = itr.next.next
            itr=itr.next       
        
        
    
    # here since we are just taking data of node, 2 while loop are required
    
    # def replace_max(self, value): 
    #     itr = self.head
    #     max=itr.data
    #     count1=0
    #     index = 0
    #     while itr:
    #         if itr.data > max:
    #             max = itr.data
    #             index = count1
    #         count1+=1
    #         itr = itr.next
    #     count2=0
    #     itr = self.head
    #     while itr:
    #         if count2 == index:
    #             itr.data = value
    #             break
    #         itr=itr.next
    #         count2+=1
            
        
                
    
# root=LinkedList()
# root.insert_at_end(12)
# root.insert_at_end(18)
# root.insert_at_end(98)
# root.insert_at_end(188)
# root.insert_at_end(19)
# root.insert_at_end(134)
# print(root.printf())
# root.replace_max_efficient(10)
# print(root.printf())
# print(root.sum_odd_indexes())
# root.reverse()
# print(root.printf())

# Specifically for Problem 4

# word_list = LinkedList()
# word_list.insert_at_end("T")
# word_list.insert_at_end("h")
# word_list.insert_at_end("e")
# word_list.insert_at_end("/")
# word_list.insert_at_end("*")
# word_list.insert_at_end("s")
# word_list.insert_at_end("k")
# word_list.insert_at_end("y")
# word_list.insert_at_end("*")
# word_list.insert_at_end("i")
# word_list.insert_at_end("s")
# word_list.insert_at_end("/")
# word_list.insert_at_end("/")
# word_list.insert_at_end("b")
# word_list.insert_at_end("l")
# word_list.insert_at_end("u")
# word_list.insert_at_end("e")
# print(word_list.printf())
# print(word_list.traverse())
# word_list.string_manipulation()
# print(word_list.traverse())


# Specifically for Problem 5

# duplicate = LinkedList()
# duplicate.insert_at_end(1)
# duplicate.insert_at_end(1)
# duplicate.insert_at_end(1)
# duplicate.insert_at_end(3)
# duplicate.insert_at_end(3)
# print(duplicate.printf())
# duplicate.remove_duplicates_alt()
# print(duplicate.printf())
        