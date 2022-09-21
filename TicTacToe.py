from random import choice

tabela = [[1,2,3],[4,5,6],[7,8,9]]

def display(tabela):
    for linha in range(len(tabela)):
        for coluna in range(len(tabela)):
            print(f"{tabela[linha][coluna]}", end = " ")
        print("\n")
        
def escrever(tabela):
    escolha = int(input("Escolha um número:"))
    if escolha>9:
        print("número inválido")
        escrever(tabela)
    elif escolha>6:
        if tabela[2][escolha-7] == 'x'or tabela[2][escolha-7] == 'o':
            print("número inválido")
            escrever(tabela)
        else:
            tabela[2][escolha-7] = 'x'
    elif escolha>3:
        if tabela[1][escolha-4] == 'x' or tabela[1][escolha-4] == 'o':
            print("número inválido")
            escrever(tabela)
        else:
            tabela[1][escolha-4] = 'x'
    elif escolha>0:
        if tabela[0][escolha-1] == 'x' or tabela[0][escolha-1] == 'o':
            print("número inválido")
            escrever(tabela)
        else:
            tabela[0][escolha-1] = 'x'
    else:
        print("Número inválido")
        escrever(tabela)
def vitoria(tabela, sinal):
    #linha horizontal
    if tabela[0][0] == sinal and tabela[0][1] == sinal and tabela[0][2] == sinal:
        print("vitoria de ",sinal)
        return 1
    if tabela[1][0] == sinal and tabela[1][1] == sinal and tabela[1][2] == sinal:
        print("vitoria de ",sinal)
        return 1
    if tabela[2][0] == sinal and tabela[2][1] == sinal and tabela[2][2] == sinal:
        print("vitoria de ",sinal)
        return 1
    
    #linha vertical
    if tabela[0][0] == sinal and tabela[1][0] == sinal and tabela[2][0] == sinal:
            print("vitoria de ",sinal)
            return 1
    if tabela[0][1] == sinal and tabela[1][1] == sinal and tabela[2][1] == sinal:
            print("vitoria de ",sinal)
            return 1
    if tabela[0][2] == sinal and tabela[1][2] == sinal and tabela[2][2] == sinal:
            print("vitoria de ",sinal)
            return 1
            
    #Linha diagonal
    if tabela[0][0] == sinal and tabela[1][1] == sinal and tabela[2][2] == sinal:
            print("vitoria de ",sinal)
            return 1
    if tabela[0][2] == sinal and tabela[1][1] == sinal and tabela[2][0] == sinal:
            print("vitoria de ",sinal)
            return 1
def casas_livres(tabela):
    lista_livres =[]
    for linha in range(len(tabela)):
        for coluna in range(len(tabela)):
            if tabela[linha][coluna] != 'x':
                if tabela[linha][coluna] != 'o':
                    lista_livres.append([linha, coluna])
    return lista_livres            
def escolha_bot(tabela):
    escolhas = casas_livres(tabela)
    if escolhas == []:
        return 1
    escolha = choice(escolhas)
    tabela[escolha[0]][escolha[1]] = 'o'
while True:
    display(tabela)
    escrever(tabela)
    if vitoria(tabela, 'x') == 1:
        display(tabela)
        break
    if escolha_bot(tabela)==1:
        print("Empate")
        break
    if vitoria(tabela, 'o') == 1:
        display(tabela)
        break
    
