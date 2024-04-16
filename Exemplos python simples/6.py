def raiz(m):
    if m<10:
        n=float(input(f'Entre com o {m+1}º número: '))
        print(f'A raiz quadrada de {n} é {n**(1/2):.3f}')
        raiz(m+1)

raiz(0)
