def pares(n):
    if n<=200:
        if n%2==0:
            print(n, end='\t')
        pares(n+1)
        
pares(1)
