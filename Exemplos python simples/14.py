def pir(n, m):
    if m == n:
        print('*' * m)
    else:
        print('*' * m)
        pir(n, m+1)
        
n=int(input('digite um numero: '))
pir(n, 1)