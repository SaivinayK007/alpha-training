def toys(w):
    # Write your code here
    num = 0 
    w.sort()
    n = len(w)
    i = 0
    
    while i < n :
        num +=1
        minNum = w[i]
        
        j = i+1
        
        while j < n and w[j] <= minNum + 4:
            j+=1
        i = j
    return num
    

n = int(input().strip())

w = list(map(int, input().rstrip().split()))

result = toys(w)

print(result)