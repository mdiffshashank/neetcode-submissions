class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ')' : '(',
            "}" : '{',
            "]" : '['
        }
        open_set = {'(','{','['}
        stack = []
        top = 0
        for i in range(len(s)):
            if s[i] in open_set:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    top = stack.pop()
                if top != m.get(s[i]):
                    return False
        return len(stack) == 0
        