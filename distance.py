# Bibliotecas
import math
Eh_melhor = {'Tam': math.inf, 'Caminho': [], 'X': 0, 'Y': 0}


# Funcao de calcular a distancia da rota 
def calcRota(R, Mat):
    #Variaveis
    Eh_melhor = {'Tam': math.inf, 'Caminho': [], 'X': 0, 'Y': 0}
    
    # Obtem a a melhor rota da lista
    for i in R:                                # Laco para navegar entra as rotas
        soma = 0
        tam = len(i['Caminho'])                         # Obtem o tamanho da rota
        # Calcula a distancia total da rota
        for j in range(tam-1):                 # Laco para caminhar nas cidades da rota
            x = i['Caminho'][j]['PM']
            y = i['Caminho'][j+1]['PM']
            soma += Mat[x][y]                  # Obtem a distancia entre duas cidades
        # Salva a melhor rota
        if(soma < Eh_melhor['Tam']):           # Confre se o novo valor é o melhor
            Eh_melhor['Caminho'] = i['Caminho']
            Eh_melhor['Tam'] = soma
            Eh_melhor['X'] = i['X']
            Eh_melhor['Y'] = i['Y']

    return Eh_melhor

def calcRotaT(R, Mat, X, Y):
    #Variaveis
    soma = 0
    tam = len(R)                         # Obtem o tamanho da rota

    # Calcula a distancia total da rota
    for i in range(tam-1):
        x = R[i]['PM']
        y = R[i+1]['PM']
        soma += Mat[x][y]                  # Obtem a distancia entre duas cidades
    # Salva a melhor rota
    if(soma < Eh_melhor['Tam']):           # Confre se o novo valor é o melhor
        Eh_melhor['Caminho'] = R
        Eh_melhor['Tam'] = soma
        Eh_melhor['X'] = X
        Eh_melhor['Y'] = Y
    
    return Eh_melhor

        