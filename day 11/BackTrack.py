import functools

n , k = input().split(" ")
n , k  = int(n) ,int(k)


@functools.cache
def BruteForce(n , k,temp):
    if n == 0 and temp >=k : return 1
    if n == 0 and temp < k: return 0

    return BruteForce(n-1,k,temp ) + BruteForce(n-1,k,temp +1 )


@functools.cache
def BackTrack(n , k ,temp):
    if n == 0 and temp >=k : return 1
    if n + temp < k : return 0 # terminates the step and reverts back to previous recursion 
    # To produce efficient code


    return BackTrack(n-1,k,temp) + BackTrack(n- 1,k ,temp + 1)














print(BruteForce(n,k,0))

print(BackTrack(n,k,0))
