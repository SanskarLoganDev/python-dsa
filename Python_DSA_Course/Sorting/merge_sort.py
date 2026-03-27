# Merge sort with time complexity O(nlogn) and space complexity o(n)

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([5,1,1,2,0,0]))


# Optimising space here, we are not creating the result array again and again, space complexity is still O(N) as we are using left_arr and right_arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr  = arr[:mid]   # O(n) — this copy is still made
    right_arr = arr[mid:]

    # recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge back INTO arr using i, j, k pointers
    i = 0  # left_arr idx
    j = 0  # right_arr idx
    k = 0  # merged array idx (writes back into arr)

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1