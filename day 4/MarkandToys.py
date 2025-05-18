def MarkAndToys(prices , amt):
    s = 0
    i =0 
    while i < len(prices) and s + prices[i] <= amt :
        s += prices[i]
        i+=1
    return i