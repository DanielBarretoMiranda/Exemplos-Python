def m1000(m, ac1000, ab1000):
    if m<10:
        n=float(input(f'Entre com o {m+1}º número: '))
        if n<1000:
            ab1000+=1
        elif n>1000:
            ac1000+=1
        m1000(m+1, ac1000, ab1000)
    else:
        print(f'A quantidade de números digitados acima de 1000 é {ac1000}!')
        print(f'A quantidade de números digitados abaixo de 1000 é de {ab1000}!')
        print(f'A quantidade de números digitados iguais a 1000 é de {m-(ac1000+ab1000)}!')
m1000(0, 0, 0)