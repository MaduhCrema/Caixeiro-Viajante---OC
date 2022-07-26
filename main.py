# Bibliotecas
import sys
from calr_first import calcRota
from rotas import makeRoute

# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')

# Variáveis
matrizAux = []
Rota_Inicial = []
Matriz_Dist = []
Teste = []

# Pega o número de cidades
n_linhas = int(arquivo.readline().rstrip())
print(n_linhas)

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

# Matriz Oficial
for i in range(n_linhas):
    for j in range(n_linhas):
        s = [str(integer) for integer in matrizAux[i][j]]
        a_string = "".join(s)
        res = int(a_string)

        Matriz_Dist[i][j] = res


# print de teste
print("=====================MATRIZ===============================")
print("[", end='')
for i in range(n_linhas):
    for j in range(n_linhas):
        print(Matriz_Dist[i][j], end='')

    # formatação do print
    if(i == n_linhas-1):
        print("", end='')
    else:
        print()
print("]")

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

Teste = makeRoute(Rota_Inicial, Matriz_Dist)

print(Teste)
