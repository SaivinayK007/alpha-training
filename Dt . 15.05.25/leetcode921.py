def minAddToMakeValid(s:str):
    #using counters
    openc = 0 
    closedc = 0

    for ch in s:
        if ch == '(':
            openc+=1
        elif ch == ')' and openc > 0:
            openc -=1
        else:
            closedc +=1
    return openc + closedc

#Using Stack

def minAddtoMakeWithStack(s:str):
    stack = []
    count = 0

    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif stack == [] :
            count +=1
        else:
            stack.pop()
            
    return len(stack) + count

