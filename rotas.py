# Funcao geradora de rotas iniciais
def makeRoute(Vet, Mat):
    # Declaracao das variaveis
    n = len(Vet)
    Route = {'Caminho': [], 'X': 0, 'Y': 0}
    Possibilidades = []
    cont = 0

    # Geraca da possiblidades
    for i in range(n):                                  # Laco para navegar na posicao a ser variada
        Vaux = Vet.copy()                               # Cria uma copia do Vetor para realizar a troca
        YEP = True                                      # Flag que indica se a cidade existe ou nao
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
                        # Verifica se a rota e possivel
                        for k in range(n):
                            if(k != n-1):                # Nao existe transicao na ultima cidade, não precisa checar
                                x = Vaux[k]['PM']        # Pega a posicao na matriz da primeira ciadade
                                y = Vaux[k+1]['PM']      # Pega a posição na matriz da proxima cidade
                                if(Mat[x][y] == 0):
                                    YEP = False
                        # Adiciona a rota a lista de possibilidades caso ela exista 
                        if(YEP):
                            print(cont)
                            Route['Caminho'] = Vaux
                            print(Vaux, "\n")
                            Possibilidades.append(Vaux)
                            cont += 1
            i = aux

    for l in Possibilidades:
        print(l, "\n\n")
    return Possibilidades
