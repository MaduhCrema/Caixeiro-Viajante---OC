# Bibliotecas
import sys
from tracemalloc import start

# Abrindo Arquivo
nomeArquivo = sys.argv[1]
arquivo = open(nomeArquivo, 'r')
# variáveis
populacaoInicial = []
matrizPopulacao = []
# pega o número de cidades
n_linhas = int(arquivo.readline().rstrip())
print(n_linhas)
for linha in arquivo:
    # Dicionário
    vet = {'km - Inicial': 0.0, 'conteudo': 0.0, 'km - Final': 0.0}
    linha = str.strip(linha)
    vet['conteudo'] = linha
    populacaoInicial.append(vet)

   # Matriz
    for i in range(int(n_linhas)):
        # cria a linha i
        linhaM = []  # lista vazia
        for caractere in linha:
            caractere = str(caractere)
            linhaM += str.strip(caractere)

        # coloque linha na matriz
    matrizPopulacao += [linhaM]
# fim do arquivo
arquivo.close()
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

print("]", end='')
