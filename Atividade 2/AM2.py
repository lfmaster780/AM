arquivo = open("iris2.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
teste = []
clasT = []
for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])

    itens.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    classificacao.append(clas)

arquivo.close()

arquivo = open("iris2Teste.data","r", encoding = "utf8")
arq = arquivo.readlines()

for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])

    teste.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    clasT.append(clas)

arquivo.close()

def distancia(test,train):
    soma = 0
    for j in range(len(test)):
        mult = float(test[j])-float(train[j])
        mult = mult**2
        soma += mult

    dist = soma**(1/2)
    return dist

predicoes = []
acertos = 0

def minkowski(test,train,p):
    soma = 0
    for j in range(len(test)):
        modulo = float(test[j])-float(train[j])
        mult = modulo**p
        soma += mult

    dist = soma**(1/p)
    return dist

p = int(input("Valor de P: "))
for k in range(len(teste)):
    atual = teste[k]
    menor = 999999999
    index = -1
    for j in range(len(itens)):
        treino = itens[j]
        #dist = distancia(atual,treino)
        dist = minkowski(atual,treino,p)
        if menor > dist:
            menor = dist
            index = j

    pred = classificacao[index]
    predicoes.append(pred)
    if clasT[k] == pred: #Classificação original == predição feita
        acertos += 1

erros = 30 - acertos
taxa = (acertos/30)*100

print("ACERTOS:",acertos)
print("ERROS:",erros)
print("Taxa de Acerto:",taxa,"%")
