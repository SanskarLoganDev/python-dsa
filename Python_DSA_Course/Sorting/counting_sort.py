# Counting sort
# time complexity: O(n+k)
# Space complexity: O(n) if you use a map, O(k) if you use an array

def counting_sort(nums):
    mn = min(nums)
    mx = max(nums)
    mp = {}
    for n in nums:
        mp[n] = mp.get(n, 0)+1
    i = 0
    for num in range(mn, mx+1):
        if num in mp:
            while mp[num]>0:
                nums[i] = num
                mp[num]-=1
                i+=1
    return nums

res = counting_sort([2,66,30,5,5,59,10])
print(res)