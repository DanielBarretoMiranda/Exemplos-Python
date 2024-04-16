def tabuada(n,m):
    if m<11:
        print(f'{m} x {n} = {m*n}')
        tabuada(n,m+1)

n=float(input('Entre com um número: '))
tabuada(n,1)

