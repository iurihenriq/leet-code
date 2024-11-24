class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()

        return len(stack) == 0
