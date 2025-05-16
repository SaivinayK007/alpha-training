
def minRemoveToMakeValid( s: str) -> str:
    stack = []
    i = 0
    store = ''
    while i < len(s):
        if s[i].isalpha() : pass
        elif s[i] == '(':
            stack.append(i)
        elif stack == [] or s[stack[len(stack)-1]] !=  '(':
            stack.append(i)
        else:
            stack.pop()
        i+=1
    
    while stack != []:
        top = stack[len(stack)-1]
        s = s[:top] + s[top+1::]
        stack.pop()
    print(s)

minRemoveToMakeValid("lee(t(c)o)de)")