arquivo = open("iris4.data","r", encoding = "utf8")
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

arquivo = open("iris4Teste.data","r", encoding = "utf8")
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
total = len(teste)

def distancia(test,train):
    soma = 0
    for j in range(len(test)):
        mult = abs(float(test[j])-float(train[j]))
        mult = mult**2
        soma += mult

    dist = soma**(1/2)
    return dist

def distanciaPeso(test,train):
    soma = 0.0
    for j in range(len(test)):
        mult = abs(float(test[j])-float(train[j]))
        mult = mult**2
        soma += mult

    dist = (1/soma)**(1/2)
    return dist

predicoes = []
acertos = 0


for k in range(len(teste)):
    atual = teste[k]
    #[DISTANCIA,INDICE]
    nn7 = [[999999,-1] for n in range(7)]

    for j in range(len(itens)):
        treino = itens[j]
        dist = distancia(atual,treino)
        if nn7[0][0] > dist:
            nn7[0][0] = dist
            nn7[0][1] = j
            nn7.sort()
            nn7.reverse()

    count = [0,0,0]#Iris-setosa,Iris-versicolor,Iris-virginica
    #Somando 1/distancia de cada pra dar o peso de cada classe
    for i in range(7):
        index = nn7[i][1]
        clas = classificacao[index]
        d = nn7[i][0]
        if clas == "Iris-setosa":
            count[0] += 1/d
        elif clas == "Iris-versicolor":
            count[1] += 1/d
        else:
            count[2] += 1/d

    pred = ""
    if count[0] >= count[1] and count[0] >= count[1]:
        pred = "Iris-setosa"
    elif count[1] >= count[0] and count[1] >= count[2]:
        pred = "Iris-versicolor"
    else:
        pred = "Iris-virginica"

    predicoes.append(pred)
    if clasT[k] == pred: #Classificação original == predição feita
        acertos += 1
'''
for k in range(len(teste)):
    atual = teste[k]
    #[DISTANCIA,INDICE]
    nn7 = [[999999,-1] for n in range(7)]

    for j in range(len(itens)):
        treino = itens[j]
        dist = distancia(atual,treino)
        if nn7[0][0] > dist:
            nn7[0][0] = dist
            nn7[0][1] = j
            nn7.sort()
            nn7.reverse()

    count = [0,0,0]#Iris-setosa,Iris-versicolor,Iris-virginica
    for i in range(7):
        index = nn7[i][1]
        clas = classificacao[index]
        if clas == "Iris-setosa":
            count[0] += 1
        elif clas == "Iris-versicolor":
            count[1] += 1
        else:
            count[2] += 1

    pred = ""
    if count[0] >= count[1] and count[0] >= count[1]:
        pred = "Iris-setosa"
    elif count[1] >= count[0] and count[1] >= count[2]:
        pred = "Iris-versicolor"
    else:
        pred = "Iris-virginica"

    predicoes.append(pred)
    if clasT[k] == pred: #Classificação original == predição feita
        acertos += 1
'''
erros = total - acertos
taxa = (acertos/total)*100

print("ACERTOS:",acertos)
print("ERROS:",erros)
print("Taxa de Acerto:",taxa,"%")
