class Solution:
    def isValid(self, s: str) -> bool:
        chars = ['(', ')', '[', ']', '{', '}']
        stack = []

        closing_to_opening = {
            chars[1] : chars[0],
            chars[3] : chars[2],
            chars[5] : chars[4],  
        }
        for ch in s:
            if ch in closing_to_opening:
                if len(stack) == 0:
                    return False
                # Check if the top of stack matches the required opening bracket
                if stack[-1] != closing_to_opening[ch]:
                    return False
                    
                # Matched pair -> pop the opening bracket
                stack.pop()
            else:
                # ch is an opening bracket -> push it
                stack.append(ch)

        # Valid only if nothing is left unmatched
        return len(stack) == 0

