import pyodbc
import os
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| MENU DAROÇA                                                 |')
    print('|                                                             |')
    print('| Murilo & Vinicius                                           |')
    print('|                                                             |')
    print('| Versão 1.0 de 28/maio/2024                                  |')
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
    
    command = f"SELECT * FROM daroca.produtos WHERE nome='{nom}'"
        
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
        nome=input('\nNome do produto: ').lower().title()

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD or dados_selecionados!=[]:
            print ('Produto já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    imagem   = input('Imagem: ')
    valor   = input('Valor: ')
    descricao    = input('Descrição: ')
    categoria      = input('Categoria: ')
    
    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO daroca.produtos "+\
                 "(nome,imagem,valor,descricao,categoria) "+\
                 "VALUES"+\
                f"('{nome}','{imagem}','{valor}','{descricao}','{categoria}')"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")


def atualizar():
    digitouDireito = False
    while not digitouDireito:
        nome = input('Nome do produto que você deseja atualizar: ').lower().title()

        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM daroca.produtos WHERE nome = '{nome}'")
        dados_selecionados = cursor.fetchall()

        if not dados_selecionados:
            print('Produto inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print("\nAtualizando os dados de:", nome)

    opcoesAtualizacao = ['Atualizar imagem', 'Atualizar valor', 'Atualizar descrição', 'Atualizar categoria', 'Finalizar atualizações']

    while True:
        opcao_atualizacao = opcaoEscolhida(opcoesAtualizacao)

        if opcao_atualizacao == '5':
            break
        elif opcao_atualizacao == '1':
            novaImagem = input("Digite a nova imagem: ")
            cursor.execute(f"UPDATE daroca.produtos SET imagem = '{novaImagem}' WHERE nome = '{nome}'")
            connection.commit()
            print("Nova imagem atualizada com sucesso!")

        elif opcao_atualizacao == '2':
            novoValor = input("Digite o novo valor: ")
            cursor.execute(f"UPDATE daroca.produtos SET valor = '{novoValor}' WHERE nome = '{nome}'")
            connection.commit()
            print("Novo valor atualizado com sucesso!")

        elif opcao_atualizacao == '3':
            novaDescricao = input("Digite a nova descrição: ")
            cursor.execute(f"UPDATE daroca.produtos SET descricao = '{novaDescricao}' WHERE nome = '{nome}'")
            connection.commit()
            print("Nova descrição atualizada com sucesso!")
        elif opcao_atualizacao == '4':
            novaCategoria = input("Digite a nova categoria: ")
            cursor.execute(f"UPDATE daroca.produtos SET categoria = '{novaCategoria}' WHERE nome = '{nome}'")
            connection.commit()
            print("Nova categoria atualizada com sucesso!")

    print("\nAtualizações feitas com sucesso!")
     

def excluir ():
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome do produto: ').lower().title()

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD:
            print("Sem conexão com o BD!")
        elif dados_selecionados==[]:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
            
    print('Imagem: ',dados_selecionados[0][2])
    print('Valor: ',dados_selecionados[0][3])
    print('Descricao: ',dados_selecionados[0][4])
    print('Categoria: ',dados_selecionados[0][5])
    
    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        try:
            #cursor e um objeto que permite que 
            #nosso programa executre comandos SQL
            #la no sevidor
            cursor = connection.cursor()

            command= "DELETE FROM daroca.produtos "+\
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

menu=['Incluir Produto',\
      'Atualizar Produto',\
      'Excluir Produto',\
      'Sair do Programa']

opcao=666
while opcao!=4:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir()
    elif opcao==2:
        atualizar()
    elif opcao==3:
        excluir()
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
