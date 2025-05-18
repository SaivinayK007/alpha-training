def evalRPN(tokens) -> int:
        stack = []
        for token in tokens :
            if token.isnumeric() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
               
            elif token in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()

                if token == "+":
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 -op2)
                elif token == '*':
                    stack.append(op1 *op2)
                elif token =='/':
                    stack.append(int(op1 / op2))

        
        return stack.pop()


print(evalRPN([]))