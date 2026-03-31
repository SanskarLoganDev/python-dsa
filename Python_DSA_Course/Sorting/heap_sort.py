# Heap sort
# time complexity: O(nlogn)
# space complexity: O(1)

# left element = 2*i+1
# right element = 2*i+2
# where i is the parent

# Using max heap
# to heapify we consider the last parent node -> (n//2)-1


def heap_sort(arr):
    n = len(arr)
    # Step 1: Build max-heap (start from last non-leaf node)
    for i in range(n//2-1,-1,-1):
        max_heapify(arr, n, i)
        
    # Step 2: Extract max one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # move current max to end
        max_heapify(arr, i, 0)            # restore heap property on reduced heap
        
    return arr


def max_heapify(arr, n, i): # here n is the index up to which the heapification will tak place
    largest = i # holds the index of largest element
    left = 2*i+1
    right = 2*i+2
    
    # largest so far is compared with left child
    if left<n and arr[largest]<arr[left]:
        largest = left # update the largest element index
    
    if right<n and arr[largest]<arr[right]:
        largest = right
        
    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i] # swapping the largest element and parent
        max_heapify(arr, n, largest) # only call when the swapping takes place
    
arr = [2,66,30,5,9,10]
heap_sort(arr)
print(arr)  # will give the answer in descending order


# for i in range(n-1, 0, -1) — why not go all the way to 0?
# When i=1 there are only 2 elements left in the heap — arr[0] and arr[1]. 
# After swapping and locking arr[1], only arr[0] remains. A single element is already sorted by definition. 
# Processing i=0 would mean arr[0], arr[0] = arr[0], arr[0] — swapping an element with itself, completely pointless. So the loop correctly stops at i=1.

# arr[0], arr[i] = arr[i], arr[0] — why always index 0?
# Because max_heapify guarantees the largest element in the active heap is always bubbled to index 0 (the root). 
# So index 0 is always where the current maximum lives. 
# Swapping it with arr[i] places that maximum at position i — which is exactly where it belongs in the final sorted array, since everything to its right is already locked and larger.

# max_heapify(arr, i, 0) — what do the arguments mean?
# i is the heap size — it tells heapify "only treat indices 0 to i-1 as the active heap, ignore everything from i onwards." 
# The 0 is the starting index to heapify from — always the root, because that's the only element out of place after the swap. So i shrinks by 1 each iteration, progressively locking more elements on the right and shrinking the heap on the left.