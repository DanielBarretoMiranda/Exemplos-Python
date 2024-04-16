def mde5(n):
    if n<=500:
        if n%5==0:
            print(n, end='\t')
        mde5(n+1)
        
mde5(1)