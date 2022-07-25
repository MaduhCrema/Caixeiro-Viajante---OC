# Bibliotecas
import sys
from rotas import makeRote
from psd_calc import calcRota
# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')

# variáveis
matrizAux = []
populacaoInicial = []
matrizPopulacao = []
rotaInicial = []

# pega o número de cidades
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
    matrizPopulacao.append(linhaMP)  # criando a matriz oficial
# fim do arquivo
arquivo.close()

# Matriz Oficial
for i in range(n_linhas):
    for j in range(n_linhas):
        s = [str(integer) for integer in matrizAux[i][j]]
        a_string = "".join(s)
        res = int(a_string)

        matrizPopulacao[i][j] = res


# print de teste
print("=====================MATRIZ===============================")
print("[", end='')
for i in range(n_linhas):
    for j in range(n_linhas):
        print(matrizPopulacao[i][j], end='')

    # formatação do print
    if(i == n_linhas-1):
        print("", end='')
    else:
        print()
print("]")

# Rota inicial e População Inicial
cont = 0
for i in range(1, int(n_linhas+2)):
    rotaInicial = {'cidade': 0, 'PosicaoMatriz': 0}
    if(i == n_linhas+1):
        rotaInicial['cidade'] = (i-n_linhas)
        rotaInicial['PosicaoMatriz'] = 0
    else:
        rotaInicial['cidade'] = i
        rotaInicial['PosicaoMatriz'] = cont
    populacaoInicial.append(rotaInicial)
    cont += 1

# print(populacaoInicial)

# chama a função de fazer as trocas de cidade
possibilidades = []
possibilidades, quantidadeRotas = makeRote(
    populacaoInicial, n_linhas, matrizPopulacao)
#print(possibilidades, quantidadeRotas)
print("----------------------------------------------------------------------")
# Função calculo de distância
print(calcRota(possibilidades, matrizPopulacao, n_linhas, quantidadeRotas))
