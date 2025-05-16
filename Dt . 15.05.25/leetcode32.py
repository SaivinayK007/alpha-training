def LongestValidParentheses(s:str):
    if len(s) == 0 :
            return 0

    stack =[]
    i = 0 
    while i < len(s):
        if s[i] == '(':
            stack.append(i)
        elif stack == [] or s[stack[len(stack)-1]]!= '(':
            stack.append(i)
        else:
            stack.pop()
        i+=1

    y = len(s)
    res = 0
    while stack != []:
        res = max(res , y - stack[len(stack)-1] -1)
        y = stack[len(stack)-1]
        stack.pop()

    return max(y ,res)

''' 
   Time Complexity :O(N)
   Space Complexity:O(N)
   
'''

