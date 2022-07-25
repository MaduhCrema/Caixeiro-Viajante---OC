# Bibliotecas
import math

# Funcao de calculo da melhor rota


def calcRota(rotas_p, Mat_dist, N, nRotas):
    eh_melhor = {'Dist': math.inf,
                 'rote': [],
                 'X': 0,
                 'Y': 0
                 }

    index = len(rotas_p[0]['Caminho'])
    for i in range(nRotas-1):         # Laco para navegar entre as diferentes rotas
        soma = 0
        for j in range(index-1):      # Laco criado para navegar entre as cidades das rotas
            x = rotas_p[i]['Caminho'][j]['PosicaoMatriz']
            y = rotas_p[i]['Caminho'][j+1]['PosicaoMatriz']
            soma += Mat_dist[x][y]

        # Encontra a melhor rota
        if(soma < eh_melhor['Dist']):
            eh_melhor['Dist'] = soma
            eh_melhor['rote'] = rotas_p[i]
            eh_melhor['X'] = x
            eh_melhor['Y'] = y
    return eh_melhor
