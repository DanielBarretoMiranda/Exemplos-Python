def prim(n, m):
    def prim2(n,m):
        if n%m == 0:
            return True
        else:
            return False
    if n == m+1 or n == 2:
        print(f'{n} é primo')
    elif prim2(n,m):
        print(f'{n} não é primo')
    else:
        prim(n, m+1)
        
n = int(input('digite um número: '))
m = 2
prim(n,m)
