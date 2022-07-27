# Bibliotecas
import math

# Funcao de calcular a distancia da rota 
def calcRota(R, Mat):
    #Variaveis
    Eh_melhor = {'Tam': math.inf, 'Rota': [], 'X': 0, 'Y': 0}
    soma = 0

    # Obtem a a melhor rota da lista
    for i in R:                        # Laco para navegar entra as rotas
        Rot = i.copy()
        tam = len(Rot)                  # Obtem o tamanho da rota
        # Calcula a distancia total da rota
        for j in range(tam-1):          # Laco para caminhar nas cidades da rota
            x = Rot[j]['PM']
            y = Rot[j+1]['PM']
            soma += Mat[x][y]           # Obtem a distancia entre duas cidades
        # Salva a melhor rota
        if(soma < Eh_melhor['Tam']):
            Eh_melhor['Rota'] = Rot['Caminho']
            Eh_melhor['Tam'] = soma
            Eh_melhor['X'] = Rot['X']
            Eh_melhor['Y'] = Rot['Y']

        print(Eh_melhor, "\n")
        
        