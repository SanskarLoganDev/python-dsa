# Priority queue is not a data structure but an abstract data type that can be implemented efficiently using heap data structure
# Extract min of the heap, pop out the top  (we take the last node, put it at top) and perform sift down operation
# Insert element: sift up operation
# the nodes here can also have values attached to the node
# left = 2*index+1
# right = 2*index+2
# parent = (index+1)//2
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
    
    import heapq
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