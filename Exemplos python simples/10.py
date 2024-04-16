def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)
    
n = int(input('digite um número: '))
print(f'o fatoria de {n} = {fat(n)}')
