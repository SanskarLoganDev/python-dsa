# Quick Sort implementation in Python
# Average time complexity: O(n log n)
# Worst time complexity:   O(n^2)  — when array is already sorted and pivot is always min/max
# Space complexity:        O(log n) — recursion stack depth

# Space complexity explanation:
# Every time quick_sort calls itself, Python pushes a stack frame onto the call stack. 
# That frame holds the local variables for that call — arr, start, end, pi — and it stays alive in memory until that call returns.

# Partitioning scheme: Hoare Partition (pivot = first element)
# 1. Pick arr[start] as pivot, remember its index
# 2. Move start pointer RIGHT until we find an element > pivot
# 3. Move end pointer LEFT until we find an element <= pivot (i.e. pivot's correct side)
# 4. If pointers haven't crossed, swap arr[start] and arr[end]
# 5. Repeat until pointers cross
# 6. Swap pivot (arr[pivot_index]) with arr[end] — pivot is now in its final sorted position
# 7. Return end as the pivot's final index


def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        # hoare_partition places the pivot at its final sorted position
        # and returns that index p
        p = hoare_partition(arr, start, end)

        # p is in its final position — exclude it from both recursive calls
        quick_sort(arr, start, p - 1)   # sort left of pivot
        quick_sort(arr, p + 1, end)     # sort right of pivot


def hoare_partition(arr, start, end):
    pivot_index = start          # pivot is always the first element
    pivot = arr[pivot_index]

    while start < end:

        # move start right: skip elements that already belong on the left (<=pivot)
        while start < end and arr[start] <= pivot:
            start += 1

        # move end left: skip elements that already belong on the right (>pivot)
        while end >= 0 and arr[end] > pivot:
            end -= 1

        # pointers haven't crossed — these two elements are on the wrong sides, swap
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    # pointers have crossed — end is now the correct position for pivot
    # swap pivot from its original position to arr[end]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end   # pivot is now in its final sorted position


arr = [5, 1, 1, 2, 0, 0]
quick_sort(arr)
print(arr)   # [0, 0, 1, 1, 2, 5]