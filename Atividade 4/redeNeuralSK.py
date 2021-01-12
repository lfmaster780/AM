arquivo = open("wine.txt","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
tp = 0.5
epocas = 500
lr = 0.2

for linha in arq:
    t = linha.split(",")
    clas = int(t[0])
    t[13] = t[13].rstrip('\n')
    #t.remove(t[13])
    t.remove(t[0])
    #t = [t[0],t[1]]
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    classificacao.append(clas)

print(classificacao)
print(itens)
arquivo.close()

#Dividir treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=tp, random_state=2)

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(activation = 'logistic', solver = "sgd", hidden_layer_sizes = (13,3), learning_rate_init = lr, max_iter = epocas, verbose = 1)
clf.fit(X_train,y_train)
print(X_train[0],y_train[0])
print(X_test[0],y_test[0])

acertos = 0
erros = 0
total = len(y_test)

predicts = clf.predict(X_test)
print(predicts[0])
for k in range(len(X_test)):
    pred = predicts[k]
    if pred == y_test[k]:
        acertos += 1
    else:
        erros += 1

taxa = (acertos/total)*100
if total == acertos + erros:
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")
else:
    print("ERRO")
