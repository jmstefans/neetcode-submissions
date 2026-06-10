class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                first = stack.pop()
                second = stack.pop()
                roundedTowardZero = int(second / first)
                stack.append(roundedTowardZero)
            else:
                stack.append(int(c))
        return stack[0]
        
        
        
        
        
        
        
        
        
        #operators = ['+', '-', '*', '/']
        #stack = []
        #result = int(tokens[0])

        #for string in tokens[1:]:
        #    if string not in operators:
        #        stack.append(int(string))
        #    elif string == '+':
        #        result += stack.pop()
        #    elif string == '-':
        #        result -= stack.pop()
        #    elif string == '*':
        #        result *= stack.pop()
        #    elif string == '/':
        #        result = int(result / stack.pop())
            
        #return result