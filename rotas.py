# Funcao geradora de rotas iniciais
def makeRoute(Vet):
    # Declaracao das variaveis
    n = len(Vet)
    Route = {'Caminho': [], 'X': 0, 'Y': 0}
    Possibilidades = []
    cont = 1
     
    # Geraca da possiblidades
    for i in range(1, n-1):                         # Laco para navegar na posicao a ser variada
        Vaux = Vet.copy()                           # Cria uma copia do Vetor para realizar a troca
        aux = i
        # Laço para deslocar o valor para a direita
        for j in range(i+1, n-1):      
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

# Funcao para verificar se a rota existe
def pRoute(Rota, Mat):
    # Decalracao de Variaveis
    Routes = []                                 # Lista com as rotas possiveis
    Flag = 0                                    # Flag para indicar se a rota é possivel

    # Realiza a verificacao
    for i in Rota:
        Flag = 0                                # Garante que a flag sempre vai ser resetada a cada nova rota
        Raux = i['Caminho'].copy()
        l = len(Raux)
        # Navega por cada cidade veficando conexao com a seguinte
        for j in range(l-1):                    
            x = Raux[j]['PM']
            y = Raux[j+1]['PM']
            # Caso a rota nao exista levanta a flag
            if(Mat[x][y] == 0):                 
                Flag = 1
        # Caso a flag estaja abixada passa a rota para lista de rotas
        if(Flag == 0):                          
            Routes.append(i)
    
    return Routes
