# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # while n >= 1:
        #     is_bad = isBadVersion(n)
        #     if is_bad:
        #         latest_bad = n
        #     else:
        #         return latest_bad
        #     n -= 1
        # return latest_bad

        # middle = n

        # found_normal = False
        # while not found_normal:
        #     if isBadVersion(middle):
        #         latest_bug_version = middle
        #         middle = middle // 2
        #     else:
        #         found_normal = True
        #         normal_version = middle
        
        # diff = latest_bug_version - normal_version + 1
        
        # for i in range(diff):
        #     curr_ver = normal_version + i
        #     if isBadVersion(normal_version + i):
        #         return curr_ver

        # return curr_ver

        l, r = 0, n

        while l < r:

            mid = (l+r) // 2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


        