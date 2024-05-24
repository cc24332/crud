import pyodbc
import os
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 12/abril/2024                                 |')
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

def connect() -> bool:
    
    try:
        global connection
        connection = pyodbc.connect(
            driver = "{SQL Server}", #fabricante
            server = "143.106.250.84", #maquina onde esta o banco de dados
            database = "BD24332", #banco de dados
            uid = "BD24332", #LOGIN
            pwd = "BD24332" #SENHA
        ) # xxxxx é seu RA
        return True
    except:
        return False

def esta_cadastrado (nom):
    # cursor e um objeto que permite que 
    #nosso programa executre comandos SQL
    #la no sevidor
    cursor = connection.cursor()
    
    command = f"SELECT * FROM crud.contatos WHERE nome='{nom}'"
        
    try:
        #tentar executar o comando no banco de dados
        cursor.execute(command)
        #como select não altera nada no BD, não faz sentido pensar
        #em aplicar as alterações; por isso não tem cursor.commit()
        dados_selecionados=cursor.fetchall() #fetchall da uma listona
                                             #contendo 0 ou mais listinhas;
                                             #cada listinha seria uma linha
                                             #trazida pelo select;
                                             #neste caso, dará uma listona
                                             #contendo 0 ou 1 listinha(s);
                                             #isso pq ou nao tem o nome
                                             #procurado, ou tem 1 só vez
        return [True,dados_selecionados]
    except:
        #em caso de erro ele vai retornar falso 
        return [False,[]]

def incluir ():
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome: ').lower().title()

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD or dados_selecionados!=[]:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço: ')
    telefone   =input('Telefone: ')
    celular    =input('Celular: ')
    email      =input('E-mail: ')
    
    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO crud.contatos "+\
                 "(nome,aniversario,endereco,telefone,celular,email) "+\
                 "VALUES"+\
                f"('{nome}','{aniversario}','{endereco}','{telefone}','{celular}','{email}')"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")


def procurar():
    digitouDireito = False
    while not digitouDireito:
        nome = input('Nome: ').lower().title() # Deixar o nome todo em minúsculo para facilitar a procura do nome, e .title() para deixar toda letra do início da palavra maiúscula (estética)

        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM crud.contatos WHERE nome = '{nome}'")
        dados_selecionados = cursor.fetchall()

        if not dados_selecionados:
            print('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print("\nOs dados de", nome, "são:") # Mostrar o nome do contato

    print('Aniversário:', dados_selecionados[0][1]) # Mostrar o aniversário do contato
    print('Endereço:', dados_selecionados[0][2]) # Mostrar o endereço do contato
    print('Telefone:', dados_selecionados[0][3]) # Mostrar o telefone do contato
    print('Celular:', dados_selecionados[0][4]) # Mostrar o celular do contato
    print('E-mail:', dados_selecionados[0][5]) # Mostrar o email do contato

def atualizar():
    digitouDireito = False
    while not digitouDireito:
        nome = input('Nome da pessoa que você deseja atualizar: ').lower().title()

        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM crud.contatos WHERE nome = '{nome}'")
        dados_selecionados = cursor.fetchall()

        if not dados_selecionados:
            print('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print("\nAtualizando os dados de:", nome)

    opcoesAtualizacao = ['Atualizar aniversário', 'Atualizar endereço', 'Atualizar telefone', 'Atualizar celular', 'Atualizar e-mail', 'Finalizar atualizações']

    while True:
        opcao_atualizacao = opcaoEscolhida(opcoesAtualizacao)

        if opcao_atualizacao == '6':
            break
        elif opcao_atualizacao == '1':
            novoAniversario = input("Digite a nova data de aniversário: ")
            cursor.execute(f"UPDATE crud.contatos SET aniversario = '{novoAniversario}' WHERE nome = '{nome}'")
            connection.commit()
            print("Nova data de aniversário atualizada com sucesso!")
        elif opcao_atualizacao == '2':
            novoEndereco = input("Digite o novo endereço: ")
            cursor.execute(f"UPDATE crud.contatos SET endereco = '{novoEndereco}' WHERE nome = '{nome}'")
            connection.commit()
            print("Novo endereço atualizado com sucesso!")
        elif opcao_atualizacao == '3':
            novoTelefone = input("Digite o novo número de telefone: ")
            cursor.execute(f"UPDATE crud.contatos SET telefone = '{novoTelefone}' WHERE nome = '{nome}'")
            connection.commit()
            print("Novo número de telefone atualizado com sucesso!")
        elif opcao_atualizacao == '4':
            novoCelular = input("Digite o novo número de celular: ")
            cursor.execute(f"UPDATE crud.contatos SET celular = '{novoCelular}' WHERE nome = '{nome}'")
            connection.commit()
            print("Novo número de celular atualizado com sucesso!")
        elif opcao_atualizacao == '5':
            novoEmail = input("Digite o novo e-mail: ")
            cursor.execute(f"UPDATE crud.contatos SET email = '{novoEmail}' WHERE nome = '{nome}'")
            connection.commit()
            print("Novo e-mail atualizado com sucesso!")

    print("\nAtualizações feitas com sucesso!")
     

def listar():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM crud.contatos")
    contatos = cursor.fetchall()

    if not contatos:
        print("Ninguém foi cadastrado ainda!")
    else:
        print("\nTodos os contatos a seguir:")
        for contato in contatos:
            print()
            print('Nome:', contato[1]) # 1 representa o índice do campo 'nome' na tabela
            print('Aniversário:', contato[2]) # 2 representa o índice do campo 'aniversario' na tabela
            print('Endereço:', contato[3]) # 3 representa o índice do campo 'endereco' na tabela
            print('Telefone:', contato[4]) # 4 representa o índice do campo 'telefone' na tabela
            print('Celular:', contato[5]) # 5 representa o índice do campo 'celular' na tabela
            print('E-mail:', contato[6]) # 6 representa o índice do campo 'email' na tabela


def excluir ():
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome: ').lower().title()

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD:
            print("Sem conexão com o BD!")
        elif dados_selecionados==[]:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
            
    print('Aniversario: ',dados_selecionados[0][2])
    print('Endereco: ',dados_selecionados[0][3])
    print('Telefone: ',dados_selecionados[0][4])
    print('Celular:',dados_selecionados[0][5])
    print('E-mail: ',dados_selecionados[0][6])
    
    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        try:
            #cursor e um objeto que permite que 
            #nosso programa executre comandos SQL
            #la no sevidor
            cursor = connection.cursor()

            command= "DELETE FROM crud.contatos "+\
                    f"WHERE nome='{nome}'"

            cursor.execute(command)
            cursor.commit()
            print('Remoção realizada com sucesso!')
        except:
            print("Remoção mal sucedida!")
    else:
        print('Remoção não realizada!')


# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

sucessoNoAcessoAoBD = connect()
if not sucessoNoAcessoAoBD:
    print("Falha ao conectar-se ao SQL Severver")
    exit() # encerra o programa

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
        incluir()
    elif opcao==2:
        procurar()
    elif opcao==3:
        atualizar()
    elif opcao==4:
        listar()
    elif opcao==5:
        excluir()
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
