def removeDuplicates(s:str):
    stack = []
    i = 0 
    ans =''

    while i < len(s):
        if len(stack) == 0:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
        i+=1
    
    stack = stack[::-1]
    while stack != []:
        ans += stack[-1]
        stack.pop()
    return ans

print(removeDuplicates("abbbabaaa"))
