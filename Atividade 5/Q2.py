arquivo = open("wine.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
tp = 0.5

for linha in arq:
    t = linha.split(",")
    clas = int(t[0])
    t[13] = t[13].rstrip('\n')
    t.remove(t[13])
    t.remove(t[0])
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    classificacao.append(clas)

arquivo.close()


holdouts = 100
taxes = []
maior = [0,-1]
menor = [100,-1]

taxes3 = []
maior3 = [0,-1]
menor3 = [100,-1]
for h in range(holdouts):

    #Dividir treino e teste
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=tp)

    from sklearn.neighbors import KNeighborsClassifier
    #kn = valor do K
    kn = 1
    neigh = KNeighborsClassifier(n_neighbors=kn)
    neigh3 = KNeighborsClassifier(n_neighbors=3)
    #Treinando
    neigh.fit(X_train, y_train)

    total = len(X_test)
    acertos = 0
    erros = 0

    predicts = neigh.predict(X_test)
    for k in range(len(X_test)):
        pred = predicts[k]
        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1

    taxa = (acertos/total)*100
    taxes.append(taxa/100)
    print("1-NN")
    if taxa >= maior[0]:
        maior = [taxa,h]
    if taxa <= menor[0]:
        menor = [taxa,h]
    if total == acertos + erros:
        print("Teste",h+1)
        print("Taxa de Acerto:",taxa,"%")
    else:
        print("ERRO")

    #3-NN
    neigh3.fit(X_train, y_train)
    total = len(X_test)
    acertos = 0
    erros = 0

    predicts = neigh3.predict(X_test)
    for k in range(len(X_test)):
        pred = predicts[k]
        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1

    taxa = (acertos/total)*100
    taxes3.append(taxa/100)
    print("")
    print("3-NN")
    if taxa >= maior3[0]:
        maior3 = [taxa,h]
    if taxa <= menor3[0]:
        menor3 = [taxa,h]
    if total == acertos + erros:
        print("Teste",h+1)
        print("Taxa de Acerto:",taxa,"%")
    else:
        print("ERRO")
    print("------------------------")

print("1-NN")
media = sum(taxes)/len(taxes)
som = 0
for g in range(len(taxes)):
    quadrado = (taxes[g]-media)**2
    som += quadrado

som = som/len(taxes)
desvio = som**(1/2)
intervaloC = [(media-(1.96*desvio))*100,(media+(1.96*desvio))*100]
print("Media da Acuracia:",media*100,"%")
print("Desvio:",desvio*100,"%")
print("Maior:",maior[0],"Menor:",menor[0])
print("Intervalo de Confianca:", intervaloC)

print("3-NN")
media = sum(taxes3)/len(taxes3)
som = 0
for g in range(len(taxes3)):
    quadrado = (taxes3[g]-media)**2
    som += quadrado

som = som/len(taxes3)
desvio = som**(1/2)
intervaloC = [(media-(1.96*desvio))*100,(media+(1.96*desvio))*100]
print("Media da Acuracia:",media*100,"%")
print("Desvio:",desvio*100,"%")
print("Maior:",maior3[0],"Menor:",menor3[0])
print("Intervalo de Confianca:", intervaloC)

print("-------------------------------")
diff = []
for y in range(len(taxes)):
    dif = taxes[y]-taxes3[y]
    diff.append(dif)

print("Diferencas:")
print(diff)

media = sum(diff)/len(diff)
som = 0
for g in range(len(diff)):
    quadrado = (diff[g]-media)**2
    som += quadrado

som = som/len(diff)
desvio = som**(1/2)
intervaloC = [(media-(1.96*desvio)),(media+(1.96*desvio))]
print("Media da Diferença:",media*100,"%")
print("Desvio:",desvio*100,"%")
print("Intervalo de Confianca:", intervaloC)

if 0 >= (media-(1.96*desvio)) and 0 <= (media+(1.96*desvio)):
    print("Os classificadores não têm acuracia significamente maior do que o outro")
elif (media-(1.96*desvio)) > 0:
    pritn("Classificador 1-NN tem acuracia significamente maior")
else:
    pritn("Classificador 3-NN tem acuracia significamente maior")
