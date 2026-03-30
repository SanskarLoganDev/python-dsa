# Quick Sort implementation in Python
# average time complexity; O(nlogn)
# Worst time complexity: O(n^2)
# space complexity: O(logn)

# partitioning scheme -> Hoare Partition
def quick_sort_hoare(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Hoare partition returns a different index than Lomuto
        # IMPORTANT: unlike Lomuto, pivot_idx is NOT necessarily in its final position
        # so we include it in BOTH recursive calls (low to p, and p+1 to high)
        p = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, p)        # includes p, unlike Lomuto
        quick_sort_hoare(arr, p + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[(low + high) // 2]   # middle element as pivot VALUE (not index)

    i = low - 1    # left pointer, moves right
    j = high + 1   # right pointer, moves left

    while True:
        # move i right until we find element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # move j left until we find element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # pointers crossed — partition done
        if i >= j:
            return j       # return j as the partition index

        # swap the out-of-place elements
        arr[i], arr[j] = arr[j], arr[i]


arr = [5, 1, 1, 2, 0, 0]
quick_sort_hoare(arr)
print(arr)   # [0, 0, 1, 1, 2, 5]