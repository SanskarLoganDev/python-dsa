# Priority queue is not a data structure but an abstract data type that can be implemented efficiently using heap data structure
# Extract min of the heap, pop out the top  (we take the last node, put it at top) and perform sift down operation
# Insert element: sift up operation
# the nodes here can also have values attached to the node
# left = 2*index+1
# right = 2*index+2
# parent = (index+1)//2
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)
    
    def __repr__(self): # with repr you can simply use print instead of using print(min_heap.string_value())
        return str(self.heap)
    
    # O(log n)
    def insert(self, key, value):
        # add it to the end
        self.heap.append([key, value])
        # sift it up the tree to properly set it
        self._sift_up(len(self.heap)-1) 
    
    # O(1)
    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]
    
    # O(log n)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        min_element = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0) # rearranging the heap using sift_down 
            # as we removed the min node from the top
            
        return min_element
    
    # O(n)    
    def heapify(self, elements):
        self.heap = list(elements)
        
        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)
        
    # O(n)
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)
    
    # O(1)
    def _parent(self, index):
        return (index+1)//2 if index!=0 else None
    
    # O(1)
    def _left(self, index):
        left = 2*index+1
        return left if left<len(self.heap) else None
    
    # O(1)
    def _right(self, index):
        right = 2*index+2
        return right if right<len(self.heap) else None
    
    # O(log n)
    def _sift_up(self, index):
        # swim: you start from the bottom
        parent_index = self._parent(index)
        
        # comparing with the parent
        while parent_index is not None and self.heap[index][0]<self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)
            
    # O(log n)
    def _sift_down(self, index):
        # sink: you start from the top
        while True:
            smallest = index
            
            left = self._left(index)
            right = self._right(index)
            # comparing with the both the children
            if left is not None and self.heap[left][0]<self.heap[smallest][0]:
                smallest = left
            if right is not None and self.heap[right][0]<self.heap[smallest][0]:
                smallest = right
                
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    
if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print(min_heap)
    
    
    mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(mylist)
    print(mylist)
    
    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())
    
    min_heap.insert(2, '2')
    print(min_heap)
    
    heapq.heappush(mylist, 2)
    print(mylist)
    
    min_heap_2 = MinHeap()
    min_heap_2.heapify([[5,'5'], [7,'7'], [2,'2']])
    min_heap.meld(min_heap_2)
    print(min_heap)
    
# Detailed Explanation of heapify
# The heapify function is one of the most important and sometimes confusing parts of heap implementations. Let’s look at the code and then explain it:

# def heapify(self, elements):
#     self.heap = list(elements)
    
#     for i in reversed(range(self._parent(len(self.heap)-1) + 1)):
#         self._sift_down(i)


# Step 1: Copying the Elements

# self.heap = list(elements)
# This line takes the input list elements and makes a copy of it into self.heap. Now the heap contains all the elements we want to build a heap from.


# Step 2: Identify the Last Parent Node

# Before we “sift down” nodes, we need to know where the non-leaf nodes (parents) are located. In an array representation of a heap:

# The leaves start at index floor(n/2) (for 0-indexed arrays).

# You want to call _sift_down on all nodes that have at least one child.

# The code uses:

# for i in reversed(range(self._parent(len(self.heap)-1) + 1)):
# len(self.heap) - 1 is the index of the last element.

# self._parent(len(self.heap)-1) returns the parent index of the last element.

# Adding 1 and then taking reversed(range(...)) produces a sequence from that parent's index down to 0.

# For example, with 10 elements, if we assume the parent of the last index (9) is computed by (9+1)//2 = 10//2 = 5, then range(self._parent(9)+1) becomes range(6), which yields indices 0,1,2,3,4,5. Reversed, we iterate: 5, 4, 3, 2, 1, 0.


# Step 3: Sift Down Each Parent

# For each index i (from the last parent to the root), we call:

# self._sift_down(i)
# The purpose of _sift_down(i) is to ensure that the subtree rooted at index i is a valid min-heap.

# It does this by comparing the node at index i with its children (found via _left(i) and _right(i)) and swapping it with the smallest child if needed.

# Then it repeats the process for the child’s new position until the subtree satisfies the min-heap property.