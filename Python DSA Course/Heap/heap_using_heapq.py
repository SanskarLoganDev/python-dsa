import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
# insert is logarithmic which is better than sorted

# Min heap
heapq.heapify(data)
print(data)

print(heapq.heappop(data)) # pops the minimum value and heapifies it
print(data)

heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)
print(data)

# Max heap
data = [-x for x in data]
print(data)

heapq.heapify(data)
print(data) # mod/abs of the value at top is the maximum

copy_data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
# Undocumented methods
heapq._heapify_max(copy_data)
print(copy_data)

print(heapq._heappop_max(copy_data)) # pops the maximum value and heapifies it
print(copy_data)

# Combining 2 heaps/lists and heapifying

l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]

l3 = heapq.merge(l1, l2)

print(list(l3))
