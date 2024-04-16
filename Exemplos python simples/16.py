def pot(n,m):
    if n== 0 and  m <=0:
        return 'inderteminado'
    if n == 0 and m > 0:
        return 0
    if n != 0 and m == 0:
        return 1
    if n != 0 and m >= 0:
        if m == 1:
            return n
        else:
            return pot(n,m-1) * n
            


n = int(input('digite um numero: '))
m= int(input('digite outro numero: '))
print(f' {n}^{m} = {pot(n,m)}')
