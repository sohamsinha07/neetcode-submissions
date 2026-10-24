class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #append everything to a stack until you hit a unique character or the end of the list
        #then pop the two elements in the stack above the unique character and conduct the operation
        #push the result onto the stack and continue
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack.pop()