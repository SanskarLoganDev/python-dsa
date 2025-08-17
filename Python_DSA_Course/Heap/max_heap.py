class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements.
        # Each element is stored as a [key, value] pair.
        self.heap = []
    
    def __len__(self):
        # Return the number of elements in the heap.
        return len(self.heap)
    
    def __repr__(self):
        # Return the string representation of the heap list.
        # This allows us to print the heap directly.
        return str(self.heap)
    
    def insert(self, key, value):
        # Insert a new element into the heap.
        # 1. Append the new element at the end of the list.
        self.heap.append([key, value])
        # 2. Restore the heap property by "sifting up" the new element.
        self._sift_up(len(self.heap) - 1)
    
    def peek_max(self):
        # Return the maximum element (the root of the heap)
        # without removing it.
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]
    
    def extract_max(self):
        # Remove and return the maximum element from the heap.
        if not self.heap:
            raise IndexError("Empty Heap")
        max_element = self.heap[0]            # Save the root (largest element)
        last_element = self.heap.pop()          # Remove the last element
        if self.heap:
            self.heap[0] = last_element         # Move the last element to the root
            self._sift_down(0)                  # Restore the heap property from the root downwards
        return max_element
    
    def heapify(self, elements):
        # Build a max-heap from an arbitrary list of elements.
        # Copy the given list into the heap.
        self.heap = list(elements)
        
        # Determine the index of the last parent node.
        # For a 0-indexed array, the parent of the last element at index (n-1)
        # is given by (n-1-1)//2 = (n-2)//2.
        # Alternatively, we can call our helper _parent on the last index.
        last_parent = self._parent(len(self.heap) - 1)
        
        # Process all non-leaf nodes from the last parent down to index 0.
        # reversed(range(last_parent + 1)) iterates from last_parent down to 0.
        for i in reversed(range(last_parent + 1)):
            self._sift_down(i)
    
    def meld(self, other_heap):
        # Merge another max-heap into this heap.
        # Combine the two lists and then rebuild the heap.
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)
    
    def _parent(self, index):
        # For a 0-indexed array, the parent index of node at index i is:
        # (i - 1) // 2. If index is 0 (the root), return None.
        return (index - 1) // 2 if index > 0 else None
    
    def _left(self, index):
        # The left child's index is given by 2*i + 1.
        left = 2 * index + 1
        return left if left < len(self.heap) else None
    
    def _right(self, index):
        # The right child's index is given by 2*i + 2.
        right = 2 * index + 2
        return right if right < len(self.heap) else None
    
    def _sift_up(self, index):
        # "Sift up" the element at the given index to restore the max-heap property.
        # While the current node exists and its key is greater than its parent's key:
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index][0] > self.heap[parent_index][0]:
            # Swap the current node with its parent.
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Move up to the parent's index.
            index = parent_index
            parent_index = self._parent(index)
    
    def _sift_down(self, index):
        # "Sift down" the element at the given index to restore the max-heap property.
        # Repeatedly compare the node with its children and swap with the larger child.
        while True:
            largest = index  # Assume current node is largest
            left = self._left(index)
            right = self._right(index)
            
            # If left child exists and its key is greater than current, update largest.
            if left is not None and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            
            # If right child exists and its key is greater than current largest, update largest.
            if right is not None and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            
            # If the largest value is still at the current index, we are done.
            if largest == index:
                break
            
            # Otherwise, swap current node with the largest child.
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Update index to continue sifting down.
            index = largest

if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print("Max heapified: ",max_heap)
    
    import heapq
    mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(mylist)
    print("Max heapified using heapq: ",mylist)
    
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    
    max_heap.insert(2, '2')
    print(max_heap)
    
    heapq.heappush(mylist, 2)
    print(mylist)
    
    max_heap_2 = MaxHeap()
    max_heap_2.heapify([[5,'5'], [7,'7'], [2,'2']])
    max_heap.meld(max_heap_2)
    print(max_heap)