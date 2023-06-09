# wheels
 Building wheels

# How to use

## Write codes in **in.py**

``` Python
# -*- coding: utf-8 -*-
from boristown.BinarySearcher import *

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        bs = BinarySearcher()
        def check(x):
            ans = 0
            i=0
            while i < n - 1:
                gap = nums[i+1] - nums[i]
                if gap <= x:
                    ans += 1
                    i += 2
                else:
                    i += 1
            return ans >= p
        return bs.search_min(check, 0, nums[-1] - nums[0])
```

## run **pycombine.bat**

## See generated code in **out.py**

``` Python
# -*- coding: utf-8 -*-
#from boristown.BinarySearcher import *

class BinarySearcher:
    def __init__(self, nums=None):
        self.nums = nums
        if nums is not None:
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
    
    def search_min(self, check, l, r):
        #find the minimum x witch check(x) is True
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        bs = BinarySearcher()
        def check(x):
            ans = 0
            i=0
            while i < n - 1:
                gap = nums[i+1] - nums[i]
                if gap <= x:
                    ans += 1
                    i += 2
                else:
                    i += 1
            return ans >= p
        return bs.search_min(check, 0, nums[-1] - nums[0])
```