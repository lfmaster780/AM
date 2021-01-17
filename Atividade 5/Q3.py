arquivo = open("wine.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
#tp = teste part, quantidade da base que será usada como teste
tp = 0.5

for linha in arq:
    t = linha.split(",")
    clas = int(t[0])
    t[13] = t[13].rstrip('\n')
    t.remove(t[0])
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    classificacao.append(clas)

arquivo.close()

holdouts = 30
intervalos = []

for ks in range(1,16):
    taxes = []
    maior = [0,-1]
    menor = [100,-1]
    print("K =",ks)
    for h in range(holdouts):

        #Dividir treino e teste
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=tp)

        from sklearn.neighbors import KNeighborsClassifier
        #ks = valor do K
        neigh = KNeighborsClassifier(n_neighbors=ks)
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
            print("Teste",h+1)
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

    intervalos.append(intervaloC)
    print("--------------------------------------------")
    print("============================================")

for k in range(len(intervalos)):
    print("Intervalo k =",k+1)
    print(intervalos[k])
    print("")
