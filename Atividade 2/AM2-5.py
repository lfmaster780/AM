#Setosa = 1 , versicolor = 2, virginica = 3

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
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    if clas == "Iris-setosa":
        clas = 1
    elif clas == "Iris-versicolor":
        clas = 2
    else:
        clas = 3
    classificacao.append(clas)

arquivo.close()

arquivo = open("iris4Teste.data","r", encoding = "utf8")
arq = arquivo.readlines()

for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])
    for j in range(len(t)):
        t[j] = float(t[j])

    teste.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    if clas == "Iris-setosa":
        clas = 1
    elif clas == "Iris-versicolor":
        clas = 2
    else:
        clas = 3
    clasT.append(clas)

arquivo.close()
total = len(teste)

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=7)
#Treinando
neigh.fit(itens, classificacao)

#Teste
acertos = 0
erros = 0

predicts = neigh.predict(teste)
for k in range(len(teste)):
    pred = predicts[k]
    if pred == clasT[k]:
        acertos += 1
    else:
        erros += 1

taxa = (acertos/total)*100

print("ACERTOS:",acertos)
print("ERROS:",erros)
print("Taxa de Acerto:",taxa,"%")
