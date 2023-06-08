
class BinarySearcher:
    def __init__(self, nums=None):
        self.nums = nums
        self.n = len(nums)
    
    def bisect_left(self, x, l, r):
        #find the first index of v in nums[l:r+1] witch v >= x
        if self.nums[r] < x:
            return r + 1
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l
    
    def bisect_right(self, x, l, r):
        #find the first index of v in nums[l:r+1] witch v > x
        if self.nums[r] <= x:
            return r + 1
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] <= x:
                l = mid + 1
            else:
                r = mid
        return l
        
    def range_len(self, minv, maxv, l, r):
        #find the number of v in nums[l:r+1] witch minv <= v <= maxv
        return self.bisect_right(maxv, l, r) - self.bisect_left(minv, l, r)