# Bibliotecas
from os import PRIO_PGRP
import sys
from distance import calcRota
from rotas import makeRoute
from rotas import pRoute

# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')

# Variáveis
matrizAux = []
Rota_Inicial = []           # Caso inicial
Matriz_Dist = []            # Lista com as adjacencias do grafo
Rotas = []                  # Lista com todas as rotas possiveis
Melhor = []                 # Lista com as melhores rotas em cada interacao

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

# ----------------
# Cria o cado base
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
# 1° Interacao - Tabela Tabu Nao Utilizada
# ----------------------------------------

# Cria as possiveis rotas do grafo
Rotas = makeRoute(Rota_Inicial)

# Verifica a existencia das rotas
Rotas = pRoute(Rotas, Matriz_Dist)

# Obetem a melhor rota
Melhor.append(calcRota(Rotas, Matriz_Dist))

print(Melhor[0])
