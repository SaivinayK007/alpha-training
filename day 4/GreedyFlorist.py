def getMinimumCost(k, c):
    c.sort(reverse=True)
    
    purchases = [0] * k
    totalpurchase = 0
    friend = 0
    
    for price in c:
        totalpurchase += (purchases[friend] + 1) * price
        purchases[friend] +=1
        friend  = (friend + 1) % k
    return totalpurchase

if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)