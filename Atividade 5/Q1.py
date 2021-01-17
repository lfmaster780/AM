arquivo = open("iris.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
tp = 0.5

for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    classificacao.append(clas)

arquivo.close()

holdouts = 100
taxes = []
maior = [0,-1]
menor = [100,-1]
for h in range(holdouts):

    #Dividir treino e teste
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=tp)

    from sklearn.neighbors import KNeighborsClassifier
    #kn = valor do K
    kn = 1
    neigh = KNeighborsClassifier(n_neighbors=kn)
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
    if taxa >= maior[0]:
        maior = [taxa,h]
    if taxa <= menor[0]:
        menor = [taxa,h]
    if total == acertos + erros:
        print("Teste",h)
        print("Taxa de Acerto:",taxa,"%")
    else:
        print("ERRO")
    print("------------------------")

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

with open('iris_Fim.data','w') as f2:
    for tax in taxes:
        f2.write(str(tax*100))
        f2.write("\n")
