# Funcao geradora de rotas iniciais
from distance import calcRotaT


def makeRoute(Vet):
    # Declaracao das variaveis
    n = len(Vet)
    Route = {'Caminho': [], 'X': 0, 'Y': 0}
    Possibilidades = []
     
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

    return Possibilidades

def tabRoute(Rota, MatT, MatD):
    Vet = Rota['Caminho']
    n = len(Vet)
    M = 0


    for i in range(1, n-1):
        a1 = 0
        a2 = 0
        Vaux = Vet.copy()
        x = i

        # Roteamento
        for j in range(i+1, n-1):
            aux2 = Vaux[i]
            Vaux[i] = Vaux[j]
            Vaux[j] = aux2
            
            # Encontra o Melhor
            i += 1
            y = j
            if(x > y):
                aux = x
                x = y
                y = aux
            if(MatT[x][y] == 0):
                Fl = pRouteT(Vaux, MatD)
                if(Fl == 0):
                    a1 = calcRotaT(Vaux, MatD, x, y)
            else:
                Fl = pRouteT(Vaux, MatD)
                if(Fl == 0):
                    a2 = calcRotaT(Vaux, MatD, x, y)

            # Criterio de aspiracao
            if(a2 != 0 and a1 != 0) :
                ax = a1['Tam']
                ay = a2['Tam']
                # Encontro o melhort no criterio
                if((ay*0.75)  < ax):
                    M = a2
                else:
                    M = a1
            if(a2 == 0 and a1 !=0):
                M = a1

            print("O melhor: ",M, "\n")
    return M

# Verifico se a rota tabu existe
def pRouteT(Rota, Mat):
    Flag = 0
    l = len(Rota)

    for i in range(l-1):
        x = Rota[i]['PM']
        y = Rota[i+1]['PM']

        if(Mat[x][y] == 0):
            Flag = 1
    
    return Flag

# Funcao para verificar se a rota existe
def pRoute(Rota, Mat):
    # Decalracao de Variaveis
    Routes = []                                 # Lista com as rotas possiveis
    Flag = 0                                    # Flag para indicar se a rota é possivel

    # Realiza a verificacao
    for i in Rota:
        Flag = 0                                # Garante que a flag sempre vai ser resetada a cada nova rota
        Raux = i['Caminho'].copy()              # Pega a rota a ser analizada
        l = len(Raux)
        # Navega por cada cidade veficando conexao com a seguinte
        for j in range(l-1):                    
            x = Raux[j]['PM']
            y = Raux[j+1]['PM']
            # Caso a rota nao exista levanta a flag
            if(Mat[x][y] == 0):                 
                Flag = 1
        # Caso a flag estaja abixada passa a rota para lista de rotas
        print(Flag)
        if(Flag == 0):                      
            Routes.append(i)

    return Routes  