class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #store the top element as val1, second element as val2 and pop the two values
        #identify operation and pop from stack
        #complete the operation and store value in val1
        #pop next item from stack and store value in val2
        #pop next item from stack and identify operation
        #perform operation
        #continue until tokens is empty
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
