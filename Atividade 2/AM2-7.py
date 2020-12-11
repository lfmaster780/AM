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

#Dividir treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=tp, random_state=100)

from sklearn.neighbors import KNeighborsClassifier
#kn = valor do K
kn = int(input())
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
if total == acertos + erros:
    print("Teste com o K =",kn)
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")
else:
    print("ERRO")
