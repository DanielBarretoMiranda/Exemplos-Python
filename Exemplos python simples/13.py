def verificar(n):
    def divNat(n, div, numDivs):
        if div<n:
            if n%div==0:
                numDivs.append(div)
            return divNat(n, div+1, numDivs)
        else:
            return numDivs
    divisores=divNat(n, 1, [])
    if n==sum(divisores):
        print(f'{n} é um número perfeito!')
    else:
        print(f'{n} não é um número perfeito!')
        
n=float(input('Entre com um número: '))
verificar(n)