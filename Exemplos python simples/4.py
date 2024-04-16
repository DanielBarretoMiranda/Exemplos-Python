def raiz(n):
    if n<=20:
        print(n**2, end='\t')
        raiz(n+1)
    
raiz(1)