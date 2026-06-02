class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        arr = sorted(nums)
        res = []
        n = len(arr)
        for i in range(len(arr)):
            anchor = arr[i] # -4

            # If anchor is positive, remaining numbers are >= anchor, can't sum to 0
            if anchor > 0:
                break
            # Skip duplicate anchors
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                total = anchor + arr[l] + arr[r]

                if total < 0:
                    l+=1
                elif total > 0:
                    r-= 1
                else:
                    res.append([anchor, arr[l], arr[r]])

                    l += 1
                    r -= 1

                    # Skip duplicates for l
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1

                    # Skip duplicates for r
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1
        return res
