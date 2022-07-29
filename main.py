# Bibliotecas
from os import PRIO_PGRP
import sys
from distance import calcRota
from rotas import makeRoute
from rotas import pRoute
from rotas import tabRoute
from matplotlib import pyplot as plt

# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')

# Variáveis
matrizAux = []
Rota_Inicial = []           # Caso inicial
Matriz_Dist = []            # Lista com as adjacencias do grafo
Rotas = []                  # Lista com todas as rotas possiveis
Melhor = []                 # Lista com as melhores rotas em cada interacao
Tabu = []                   # Matriz com os tabus de cada cidade
dados = []                  # Vetor parar mostrar os melhores valores entre as interacoes

# ---------------------------------------
# Le as informacoes de entrada do arquivo
# ---------------------------------------

# Pega o número de cidades
n_linhas = int(arquivo.readline().rstrip())

index = 0
for linha in arquivo:
    linha = str.strip(linha)
    linha = linha.split(' ')

# Matriz Aux
    for i in range(int(n_linhas)):
        # cria a linha i
        linhaM = []  # linha da matriz auxiliar
        linhaMP = []  # criando a matriz oficial
        for caractere in linha:
            caractere = caractere.split(' ')  # ignora o espaço
            linhaM.append(caractere)
            linhaMP.append(0)  # criando a matriz oficial
    # coloque linha na matriz
    matrizAux.append(linhaM)
    Matriz_Dist.append(linhaMP)  # criando a matriz oficial
# Fim do arquivo
arquivo.close()

# ----------------------------
# Cria a matriz de adjacencias
# ----------------------------

# Matriz Oficial
for i in range(n_linhas):
    for j in range(n_linhas):
        s = [str(integer) for integer in matrizAux[i][j]]
        a_string = "".join(s)
        res = int(a_string)

        Matriz_Dist[i][j] = res

print(Matriz_Dist)
# ------------------
# Cria a Tabela Tabu
# ------------------

# Tabela Tabu
for i in range(n_linhas):
    linhaT = []
    for j in range(n_linhas):
        linhaT.append(0)                # Inicializa a tabela como sendo 0 em todos os casos
    Tabu.append(linhaT)

# ----------------
# Cria o caso base
# ----------------

# Gera a primeira rota
for i in range(n_linhas):
    ROTA = {'Cidade': 0, 'PM': 0}       # Dicionario para indicar a cidade e sua posicao
    if(i == 0 and i == n_linhas):       # Garante que a cidade inicial seja sempre 1 e sua PM 0
        ROTA['Cidade'] = 1
        ROTA['PM'] = 0
    else:                               # Seta os valores das demais cidades
        ROTA['Cidade'] = i+1
        ROTA['PM'] = i
    Rota_Inicial.append(ROTA)
# Garantindo que a a rota termina na cidade inicial
ROTA = {'Cidade': 0, 'PM': 0}   # Dicionário criado fora do for
ROTA['Cidade'] = 1              # Setando os valores manualmente
ROTA['PM'] = 0                  # Setando os valores manualmente
Rota_Inicial.append(ROTA)

# ----------------------------------------
# 0° Interacao - Tabela Tabu Nao Utilizada
# ----------------------------------------

# Cria as possiveis rotas do grafo
Rotas = makeRoute(Rota_Inicial)

# Verifica a existencia das rotas
Rotas = pRoute(Rotas, Matriz_Dist)

print("\n Depois \n")

# Obetem a melhor rota
Melhor.append(calcRota(Rotas, Matriz_Dist))

# Atualiza a tabela Tabu
x = Melhor[0]['X']
y = Melhor[0]['Y']

if(x > y):                      # Condicional para ajustar as cordenadas do Tabu
    aux = x
    x = y
    y = aux
Tabu[x][y] = 3                  # Atualiza o Tabu
Tabu[y][x] += 1                 # Atualiza a frequencia

#Saida para o usuário
print("---------- Interação N°0 ----------\n")
Ca = []
aux = len(Melhor[0]['Caminho'])
for i in range(aux):
    Ca.append(Melhor[0]['Caminho'][i]['Cidade'])
print("Caminho: ", Ca)
print("Distância: ", Melhor[0]['Tam'])
print("Tabu:")
for i in Tabu:
    print(i)
print()

extra = Melhor[0].copy()
# ----------------------------------------------
# Demains N Interacaoes - Utilizando Tabela Tabu
# ----------------------------------------------
i_interacao = 0
z = 1
while(i_interacao <= 20):
    
    # Criando as n interacoles
    Melhor[0] = tabRoute(Melhor[0], Tabu, Matriz_Dist)

    # Atualiza a tabela Tabu
    x = Melhor[0]['X']
    y = Melhor[0]['Y']

    if(x > y):                      # Condicional para ajustar as cordenadas do Tabu
        aux = x
        x = y
        y = aux
    Tabu[x][y] = 3                  # Atualiza o Tabu
    Tabu[y][x] += 1                 # Atualiza a frequencia
    
    # Print
    print("---------- Interação N°", z, "----------\n")
    Ca = []
    aux = len(Melhor[0]['Caminho'])
    for i in range(aux):
        Ca.append(Melhor[0]['Caminho'][i]['Cidade'])
    print("Caminho: ", Ca)
    print("Distância: ", Melhor[0]['Tam'])
    print("Tabu:")
    for i in Tabu:
        print(i)
    print()

    z += 1

    # Dados grafico
    dados.append(Melhor[0]['Tam'])

    # Parada
    if(Melhor[0] == extra):
        i_interacao += 1
    else:
        i_interacao = 0
        extra = Melhor[0].copy()

print("DADOS", dados)

# plotagem de gráfico
plt.plot(range(len(dados)), dados)
plt.grid(True, zorder=0)
plt.title("Elitismo do fitness")
plt.xlabel("Quantidade de Fitness")
plt.ylabel("Valor do fitness")
plt.show()