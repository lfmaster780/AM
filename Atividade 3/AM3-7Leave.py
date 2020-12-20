arquivo = open("wine.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
tp = 0.1

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
tt = len(classificacao) - 1
from sklearn.neighbors import KNeighborsClassifier
#kn = valor do K
kn = 1
neigh = KNeighborsClassifier(n_neighbors=kn)
taxes = []
for x in range(tt):
    #Dividir treino e teste
    testeC = classificacao[0]
    teste = [itens[0]]

    itens[0] = [0]
    classificacao[0] = -1

    classificacao.remove(classificacao[0])
    itens.remove(itens[0])

    #Treinando
    neigh.fit(itens, classificacao)

    total = len(classificacao)
    acertos = 0
    erros = 0

    predicts = neigh.predict(teste)
    for k in range(len(teste)):
        pred = predicts[k]
        if pred == testeC:
            acertos += 1
        else:
            erros += 1

    taxa = (acertos/1)*100
    taxes.append(taxa)

    print("Teste", x+1,":",)
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")
    print("------------------------------------------")


    itens.append(teste[0])
    classificacao.append(testeC)

media = sum(taxes)/len(taxes)
print("Taxa Media:",media,"%")
