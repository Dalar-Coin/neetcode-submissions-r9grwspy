class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] == operands[0]:
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == operands[1]:
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tokens[i] == operands[2]:
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == operands[3]:
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]