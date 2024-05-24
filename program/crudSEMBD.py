def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Murilo Sanches Santana                                      |')
    print('|                                                             |')
    print('| Versão 2.0 de 19/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom==agd[meio][0]:
            return [True,meio]
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
            
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome: ').lower().title() # Deixar o nome todo em minusculo para facilitar a procura do nome, e .title() para deixar toda letra do inicio da palavra maiusculo (estética)

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço: ')
    telefone   =input('Telefone: ')
    celular    =input('Celular: ')
    email      =input('E-mail: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome: ').lower().title() # Deixar o nome todo em minusculo para facilitar a procura do nome, e .title() para deixar toda letra do inicio da palavra maiusculo (estética)

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou: # Se não achou o contato, printa a mensagem:
            print ('Pessoa inexistente - Favor redigitar...')
        else: # Caso ao contrário, mostra os dados do contato:
            digitouDireito=True

    print("\nOs dados de", nome, "são:") # Mostrar o nome do contato
    print('Aniversário:',agd[posicao][1]) # Mostrar o aniversário do contato
    print('Endereco:',agd[posicao][2]) # Mostrar o endereço do contato
    print('Telefone:',agd[posicao][3]) # Mostrar o telefone do contato
    print('Celular:',agd[posicao][4]) # Mostrar o celular do contato
    print('E-mail:',agd[posicao][5]) # Mostrar o email do contato

def atualizar(agd, posicao):
    if posicao is None: # Verifica se foi especificado uma posição para atualizar, se for none significa que o usuario ainda nao passou um contato para atualizar
        digitouDireito=False
        while not digitouDireito:
            nome=input('Nome da pessoa que você deseja atualizar: ').lower().title() # Deixar o nome todo em minusculo para facilitar a procura do nome, e .title() para deixar toda letra do inicio da palavra maiusculo (estética)
            resposta=ondeEsta(nome,agd)
            achou   = resposta[0]
            posicao = resposta[1]
        
            if not achou: # Se não achou o contato, printa a mensagem:
                print ('Pessoa inexistente - Favor redigitar...')
            else: # Caso ao contrário, mostra as opções do menu de atualização:
                digitouDireito=True

    print("\nAtualizando os dados de:", nome)
    
    while True: # Ficar repetindo até o usuário finalizar as atualizações
        opcoesAtualizacao = ['Atualizar aniversário',\
                'Atualizar endereço',\
                'Atualizar telefone',\
                'Atualizar celular',\
                'Atualizar e-mail',\
                'Finalizar atualizações'] # Opções de 1 a 6 do menu de atualização
        opcao_atualizacao = opcaoEscolhida(opcoesAtualizacao) # opcao_atualizacao vira opcaoEscolhida pra depois verificar qual foi a opção escolhida

        if opcao_atualizacao == '6': # Se digitou 6, para o while de atualizar e volta para o while do programa
            break
        if opcao_atualizacao == '1': # Se digitou 1, atualiza o aniversário
            novoAniversario = input("Digite a nova data de aniversário: ")
            agd[posicao][1] = novoAniversario # Atualiza no sistema a nova data de aniversário
            print("Nova data de aniversário atualizada com sucesso!")
        elif opcao_atualizacao == '2': # Se digitou 2, atualiza o endereço
            novoEndereco = input("Digite o novo endereço: ")
            agd[posicao][2] = novoEndereco # Atualiza no sistema o novo endereço
            print("Novo endereço atualizado com sucesso!")
        elif opcao_atualizacao == '3': # Se digitou 3, atualiza o número de telefone
            novoTelefone = input("Digite o novo número de telefone: ")
            agd[posicao][3] = novoTelefone # Atualiza no sistema o novo número de telefone
            print("Novo número de telefone atualizado com sucesso!")
        elif opcao_atualizacao == '4': # Se digitou 4, atualiza o número de celular
            novoCelular = input("Digite o novo número de celular: ")
            agd[posicao][4] = novoCelular # Atualiza no sistema o novo número de celular
            print("Novo número de celular atualizado com sucesso!")
        elif opcao_atualizacao == '5': # Se digitou 5, atualiza o email
            novoEmail = input("Digite o novo e-mail: ")
            agd[posicao][5] = novoEmail # Atualiza no sistema o novo email
            print("Novo e-mail atualizado com sucesso!")

    print("\nAtualizações feitas com sucesso!")       

def listar (agd):
    if len(agd) == 0: # Verifica se a lista está vazia, se tiver vazia mostra a msg a seguir
        print("Ninguém foi cadastrado ainda!")
    else: # caso ao contrario, vamos procurar todos os contatos da lista
        posicao = 0
        print()
        print("Todos os contatos a seguir:")
        while posicao < len(agd):
            print()
            print('Nome:', agd[posicao][0]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [0] mostra o nome
            print('Aniversário:', agd[posicao][1]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [1] mostra a data de aniversário
            print('Endereço:', agd[posicao][2]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [2] mostra o endereço
            print('Telefone:', agd[posicao][3]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [3] mostra o telefone
            print('Celular:', agd[posicao][4]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [4] mostra o celular
            print('E-mail:', agd[posicao][5]) # O [Usuario] serve como um "indice", para mostrar o dado do primeiro Usuario (primeiro indice), e [5] mostra o email
            posicao += 1

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome: ').lower().title()
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversário:',agd[posicao][1])
    print('Endereco:',agd[posicao][2])
    print('Telefone:',agd[posicao][3])
    print('Celular:',agd[posicao][4])
    print('E-mail:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda, None) # O None, serve para mostrar ao programa que ainda não tem uma posição definida, pois será o usuário que irá digitar
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')