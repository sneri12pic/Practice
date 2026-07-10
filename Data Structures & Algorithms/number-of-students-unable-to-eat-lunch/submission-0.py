class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        
        res = n
        for sandwich in sandwiches:
            i = 0
            while i < n and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                i += 1
            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else: 
                break
        return res

