# Bibliotecas
from cmath import inf

# Funcao de calculo da melhor rota


def calcRota(rotas_p, Mat_dist, N):
    eh_melhor = {'Dist': +inf,
                 'rote': [],
                 'X': 0,
                 'Y': 0
                 }

    for i in rotas_p-1:         # Laco para avegar entre as diferentes rotas
        soma = 0
        for j in range(N):      # Laco criado para navegar entre as cidades das rotas
            x = rotas_p[i][N]
            x = x['P']
            y = rotas_p[i+1][N]
            y = y['P']
            soma += Mat_dist[x][y]

            # Encontra a melhor rota
            if(soma < eh_melhor['Dist']):
                eh_melhor['Dist'] = soma
                eh_melhor['rote'] = rotas_p[i]

    return eh_melhor
