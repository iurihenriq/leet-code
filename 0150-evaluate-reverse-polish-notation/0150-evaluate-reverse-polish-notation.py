class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
                stack.append(int(t))
            else:
                result = 0
                op2 = stack.pop()
                op1 = stack.pop()

                if t == '+':
                     result = op1 + op2
                elif t == '-':
                     result = op1 - op2
                elif t == '*':
                     result = op1 * op2
                elif t == '/':
                     result = int(float(op1) / op2)

                stack.append(result)

        return stack[0]