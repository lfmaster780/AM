"""Class Values:

"no-recurrence-events", "recurrence-events"

1. Class: no-recurrence-events, recurrence-events
2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.
3. menopause: lt40, ge40, premeno.
4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59.
5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26, 27-29, 30-32, 33-35, 36-39.
6. node-caps: yes, no.
7. deg-malig: 1, 2, 3.
8. breast: left, right.
9. breast-quad: left-up, left-low, right-up, right-low, central.
10. irradiat: yes, no."""

import matplotlib.pyplot as plt
from sklearn import preprocessing, metrics, model_selection
from sklearn import tree
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import math
#LENDO ARQUIVO

itens = pd.read_csv("breast-cancer.data",encoding = "utf8", header = None)
itens.columns.tolist()
itens.rename(columns = {0:"class",1:"age",2:"menopause",3:"tumor-size",4:"inv-nodes",5:"node-caps",6:"deg-malig",7:"breast",8:"breast-quad",9:"irradiat"}, inplace = True)

classificacao = itens["class"]
#print(classificacao[0:10],"\n")

itens.drop(["class"], axis = 1,inplace = True)
#print(itens[0:10])


lenc = preprocessing.LabelEncoder()
#itens = itens.apply(lenc.fit_transform)
itens = itens.apply(lenc.fit_transform)

taxes = []
taxes2 = []
taxes3 = []
t = []
t2 = []
t3 = []
holdouts = 30

ref = ["A","B"]
refR = ["no-recurrence-events", "recurrence-events"]

for h in range(holdouts):


    #print(itens[0:10])
    print("Teste",h+1)
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=0.5)

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train,y_train)
    predicts = clf.predict(X_test)

    clf2 = tree.DecisionTreeClassifier(min_samples_leaf = 10)
    clf2.fit(X_train,y_train)
    predicts2 = clf2.predict(X_test)

    clf3 = tree.DecisionTreeClassifier(min_samples_leaf = 30)
    clf3.fit(X_train,y_train)
    predicts3 = clf3.predict(X_test)

    y_test = y_test.tolist()
    y_train = y_train.tolist()


    erros = 0
    acertos = 0
    for k in range(len(X_test)):
        pred = predicts[k]
        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1


    print("MIN LEAF 1")
    total = len(y_test)
    print("Folhas =",clf.get_n_leaves())
    taxa = (acertos/total)*100
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")

    from sklearn.metrics import confusion_matrix

    matrizC = confusion_matrix(y_test, predicts, labels=["no-recurrence-events", "recurrence-events"])
    print("Matriz:\n",refR)
    print(matrizC)

    #print("Gerando arvore construida")
    #fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
    #tree.plot_tree(clf, filled=True)
    #plt.show()
    #fig.savefig('imagename.png')
    taxes.append(taxa)
    print("")

    erros = 0
    acertos = 0
    for k in range(len(X_test)):
        pred = predicts2[k]
        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1

    print("MIN LEAF 10")
    total = len(y_test)
    print("Folhas =",clf2.get_n_leaves())

    taxa = (acertos/total)*100
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")


    matrizC = confusion_matrix(y_test, predicts2, labels=["no-recurrence-events", "recurrence-events"])
    print("Matriz:\n",refR)
    print(matrizC)

    #print("Gerando arvore construida")
    #fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
    #tree.plot_tree(clf, filled=True)
    #plt.show()
    #fig.savefig('imagename.png')
    taxes2.append(taxa)
    print("")

    erros = 0
    acertos = 0
    for k in range(len(X_test)):
        pred = predicts3[k]
        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1

    total = len(y_test)
    print("MIN LEAF 30")
    print("Folhas =",clf3.get_n_leaves())

    taxa = (acertos/total)*100
    print("ACERTOS:",acertos)
    print("ERROS:",erros)
    print("Taxa de Acerto:",taxa,"%")

    matrizC = confusion_matrix(y_test, predicts3, labels=["no-recurrence-events", "recurrence-events"])
    print("Matriz:\n",refR)
    print(matrizC)

    #print("Gerando arvore construida")
    #fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
    #tree.plot_tree(clf, filled=True)
    #plt.show()
    #fig.savefig('imagename.png')
    taxes3.append(taxa)
    print("")
    #TREINO
    total = len(y_train)

    erros = 0
    acertos = 0
    predicts = clf.predict(X_train)
    for k in range(len(X_train)):
        pred = predicts[k]
        if pred == y_train[k]:
            acertos += 1
        else:
            erros += 1



    taxa = (acertos/total)*100

    t.append(taxa)


    erros = 0
    acertos = 0
    predicts2 = clf2.predict(X_train)
    for k in range(len(X_train)):
        pred = predicts2[k]
        if pred == y_train[k]:
            acertos += 1
        else:
            erros += 1


    taxa = (acertos/total)*100

    t2.append(taxa)

    erros = 0
    acertos = 0
    predicts3 = clf3.predict(X_train)
    for k in range(len(X_train)):
        pred = predicts3[k]
        if pred == y_train[k]:
            acertos += 1
        else:
            erros += 1


    taxa = (acertos/total)*100

    t3.append(taxa)


print("----------------------------------")
print("Teste")
print("Media 1:",sum(taxes)/holdouts,"%")
print("Media 10:",sum(taxes2)/holdouts,"%")
print("Media 30:",sum(taxes3)/holdouts,"%")
print("")
print("Treino")
print("Media 1:",sum(t)/holdouts,"%")
print("Media 10:",sum(t2)/holdouts,"%")
print("Media 30:",sum(t3)/holdouts,"%")
