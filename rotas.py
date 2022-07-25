#Funcao de criar possibilidades 
def makeRote(rote_i, quant, mat):
    #Variaveis
    Possibilidades = []
    Yep = True 
    Rota = {'Caminho':[],
            'X':0,
            'Y':0
            }

    #Verifica se a rota padrao e possivel
    for k in range(quant-1):
        if(i != 0 and i != quant-2):
            x = rote_i[i]
            x = x['P']
            y = rote_i[i+1]
            y = y['P']
            if(mat[x][y] == 0):
                Yep = False
    if(Yep):
        Rota['Caminho'] = rote_i
        Rota['X'] = 0
        Rota['Y'] = 0
        Possibilidades.append(Rota)            
    
    #Gera todas as combinacoes de de rotas
    for i in range(quant-1):
        if(i != 0 and i != quant-2):
            for j in range(quant-1):
                if(j != 0 and j != quant-2):
                    aux = rote_i[j]
                    rote_i[j] = rote_i[j+1]
                    rote_i[j+1] = aux
                    x = rote_i[j]
                    x = x['P']
                    y = rote_i[j+1]
                    y = y['P']
                    
                    #Verifica se a rota e possivel
                    if(mat[x][y] != 0):
                        Rota['Caminho'] = rote_i
                        Rota['X'] = x
                        Rota['Y'] = y
                        Possibilidades.append(Rota)
                        
    return Possibilidades