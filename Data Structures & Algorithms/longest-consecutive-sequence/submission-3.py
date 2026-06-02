class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        map = {}
        for num in nums:
            map[num] = 0   # just used to dedupe keys

        arr = []
        for val in map.keys():
            arr.append(val)

        # Now arr is sorted + unique
        best = 1
        curr = 1

        res = []
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i+1]
            if a + 1 == b:
                curr += 1
            else:
                best = max(best, curr)
                curr = 1

        best = max(best, curr)
        return best


