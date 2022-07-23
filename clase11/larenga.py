def pascal(n, k):
    result=1
    if n==0:
        return result
    else:
        if k in (0, n):
         return 1
        return pascal(n-1, k-1) + pascal(n-1, k)