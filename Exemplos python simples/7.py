def menorNum(c,menor):
    if c<5:
        n=float(input(f'Entre com o {c+1}º número: '))
        if n<menor:
            menor=n
        menorNum(c+1,menor)
    else:
        print(f'O menor dos números é {menor}!')

n=float(input(f'Entre com o 1º número: '))
menorNum(1,n)

