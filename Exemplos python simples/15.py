def erroSexo():
    print('\nERRO!')
    print('Sexo não válido!')

def pedirSexo(m):
    return int(input(f'(1)Masculino \n(2)Feminino \nEntre com o sexo da {m+1}º pessoa: '))

def verificar(n,m):
    if n not in (1,2):  
        erroSexo()
        n=verificar(pedirSexo(m),m)
    return n

def infosGrupo(n,m,infos):
    if m<n:
        altura=float(input(f'Entre com a altura da {m+1}º pessoa (em metros): '))
        sexo=verificar(pedirSexo(m),m)
        infos.append([altura,sexo])
        infosGrupo(n, m+1, infos)
    return infos

def alturas(n, m, infos, soma, maior, menor, quant):
    if m<n:
        altPessoa=infos[m][0]
        soma[0]+=altPessoa
        if m==0:
            maior=altPessoa
            menor=altPessoa
        else:
            if altPessoa>maior:
                maior=altPessoa
            if altPessoa<menor:
                menor=altPessoa
        if infos[m][1]==1:
            quant[0]+=1
            soma[1]+=altPessoa
        else:
            quant[1]+=1
            soma[2]+=altPessoa
        alturas(n, m+1, infos, soma, maior, menor, quant)
    else:
        print(f'A média da altura do grupo é {soma[0]/len(infos):.2f}!')
        if quant[0]==0:
            print('Não foi computado nenhum dado para altura masculino!')
        else:
            print(f'A média da altura masculina é {soma[1]/quant[0]}')
        if quant[1]==0:
            print('Não foi computado nenhum dado para altura feminino!')
        else:
            print(f'A média da altura feminina é {soma[2]/quant[1]}')
        print(f'A maior altura do grupo é {maior}!')
        print(f'A menor altura do grupo é {menor}!')
    
def grupo(n,m,infos):
    infos=infosGrupo(n, m, infos)
    alturas(n, m, infos, [0,0,0], 0, 0, [0,0])
    
n=int(input('Entre com a quantidade de pessoas: '))
informacoes=[]
grupo(n,0,informacoes)