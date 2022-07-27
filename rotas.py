# Funcao geradora de rotas iniciais
def makeRoute(Vet):
    # Declaracao das variaveis
    n = len(Vet)
    Route = {'Caminho': [], 'X': 0, 'Y': 0}
    Possibilidades = []
    cont = 1

    # Geraca da possiblidades
    for i in range(n):                                  # Laco para navegar na posicao a ser variada
        Vaux = Vet.copy()                               # Cria uma copia do Vetor para realizar a troca
        Foi = 0                                         # Flag que indica se a cidade existe ou nao
        aux = i
        if(i != 0 and i != n-1):                        # Condicional para que os valores inicial e final não sejam alterados
            for j in range(n):                          # Laço para deslocar o valor para a direita
                if(j != 0 and j != n-1):                # Condicional para que os valores inicial e final não sejam deslocados
                    if(Vaux[i] != Vaux[j] and j > i):   # Condiocional para que apenas haja trocas para a direita
                        # Realiza a troca de cidades
                        aux2 = Vaux[i]
                        Vaux[i] = Vaux[j]
                        Vaux[j] = aux2
                        i += 1
                        # Adiciona a rota a lista de possibilidades 
                        Route = {'Caminho': [], 'X': 0, 'Y': 0}
                        Route['Caminho'] = Vaux.copy()
                        Route['X'] = aux
                        Route['Y'] = j
                        Possibilidades.append(Route)
                        cont += 1

    return Possibilidades

# def confereRota(Vet, Mat):
