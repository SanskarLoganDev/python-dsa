# Insertion sort
# time complexity: O(N^2)
# space complexity: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            j = i
            while j>0 and arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j-=1
    return arr

res = insertion_sort([2,66,30,5,9,10])
print(res)