def quantImp(m, imp):
    if m<10:
        n=int(input(f'Entre com o {m+1}º número:  '))
        if n%2!=0:
            imp+=1
        quantImp(m+1, imp)
    else:
        print(f'A quantidade de impares é de {imp}')
        
quantImp(0, 0)
        

