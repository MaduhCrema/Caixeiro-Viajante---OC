# Bibliotecas
import sys
from tracemalloc import start

# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')

# variáveis
populacaoInicial = []
matrizAux = []
matrizPopulacao = []
rotaInicial = []

# pega o número de cidades
n_linhas = int(arquivo.readline().rstrip())
print(n_linhas)
for linha in arquivo:
    # Dicionário
    vet = {'km - Inicial': 0.0, 'conteudo': 0.0, 'km - Final': 0.0}
    linha = linha.split(' ')
    vet['conteudo'] = linha
    populacaoInicial.append(vet)

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
print(populacaoInicial)
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

# Rota inicial
for i in range(1, int(n_linhas+2)):
    if(i == n_linhas+1):
        rotaInicial.append(i-n_linhas)
    else:
        rotaInicial.append(i)

print(rotaInicial)
