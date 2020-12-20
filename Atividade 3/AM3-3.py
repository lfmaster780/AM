arquivo = open("iris.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
#ts = teste size, quantidade da base que será usada como teste
ts = 0.5

for linha in arq:
    t = linha.split(",")
    t[4] = t[4].rstrip('\n')
    clas = t[4]
    t.remove(t[4])

    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    classificacao.append(clas)

arquivo.close()


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=ts)

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=1)
#Treinando
neigh.fit(X_train, y_train)

total = len(X_test)
acertos = 0
erros = 0

ref = ["A","B","C"]
refR = ["setosa","versicolor","virginica"]
# = [A,B,C] = [SETOSA,VERSICOLOR,VIRGINICA]
setosa = [0,0,0]
versicolor = [0,0,0]
virginica = [0,0,0]
matrizC = [setosa,versicolor,virginica]

predicts = neigh.predict(X_test)
for k in range(len(X_test)):
    pred = predicts[k]
    real = y_test[k]
    print("Teste",k+1,"->","Predicao:",pred,"//""Classe Real:",real)

    if real == "Iris-setosa":
        if pred == real:
            acertos += 1
            setosa[0] += 1
        elif pred == "Iris-versicolor":
            erros += 1
            setosa[1] += 1
        else:
            erros += 1
            setosa[2] += 1
    elif real == "Iris-versicolor":
        if pred == real:
            acertos += 1
            versicolor[1] += 1
        elif pred == "Iris-setosa":
            erros += 1
            versicolor[0] += 1
        else:
            erros += 1
            versicolor[2] += 1
    else:
        if pred == real:
            acertos += 1
            virginica[2] += 1
        elif pred == "Iris-setosa":
            erros += 1
            virginica[0] += 1
        else:
            erros += 1
            virginica[1] += 1



recalls =[]
precisions =[]
medidaF = []
fptaxes = []

print("--------------------------------------")
print(" ",ref[0],"",ref[1],"",ref[2]," <-- Predicted Class")
c = 0
for lines in matrizC:
    print(lines,end=" || ")
    print(ref[c],"=",refR[c])
    c+=1
#SETOSA
print("")
print("A = SETOSA")
tp = setosa[0]
fp = versicolor[0] + virginica[0]
fn = setosa[1] + setosa[2]
tn = total - tp - fp - fn

recall = tp/(tp+fn)
precision = tp/(tp+fp)
fptax = (fp/(fp+tn))*100
f = 2*precision*recall / (precision+recall)

medidaF.append(f)
fptaxes.append(fptax)
precisions.append(precision)
recalls.append(recall)

print("Recall:",recall)
print("Precisao:",precision)
print("Medida F:",f)
print("Taxa FP:",fptax,"%")

#
print("")
print("B = VERSICOLOR")
tp = versicolor[1]
fp = setosa[1] + virginica[1]
fn = versicolor[0] + versicolor[2]
tn = total - tp - fp - fn

recall = tp/(tp+fn)
precision = tp/(tp+fp)
fptax = (fp/(fp+tn))*100
f = 2*precision*recall / (precision+recall)

medidaF.append(f)
fptaxes.append(fptax)
precisions.append(precision)
recalls.append(recall)

print("Recall:",recall)
print("Precisao:",precision)
print("Medida F:",f)
print("Taxa FP:",fptax,"%")

print("")
print("C = VIRGINICA")
tp = virginica[2]
fp = setosa[2] + versicolor[2]
fn = virginica[0] + virginica[1]
tn = total - tp - fp - fn

recall = tp/(tp+fn)
precision = tp/(tp+fp)
fptax = (fp/(fp+tn))*100
f = 2*precision*recall / (precision+recall)

medidaF.append(f)
fptaxes.append(fptax)
precisions.append(precision)
recalls.append(recall)

print("Recall:",recall)
print("Precisao:",precision)
print("Medida F:",f)
print("Taxa FP:",fptax,"%")

print("")
print("Medias")
taxa = (acertos/total)*100
print("Taxa de Acerto:",taxa,"%")
print("Recall:",sum(recalls)/3)
print("Precisao:",sum(precisions)/3)
print("Medida F:",sum(medidaF)/3)
print("Taxa FP:",sum(fptaxes)/3,"%")
print("--------------------------------------")
