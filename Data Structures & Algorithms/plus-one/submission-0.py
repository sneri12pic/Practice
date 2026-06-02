class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)
        res = int(num) + 1
        r = []
        for dg in str(res):
            r.append(dg)

        return r