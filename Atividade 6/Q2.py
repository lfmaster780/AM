"""Class Values:

"unacc", "acc", "good", "vgood"

Attributes:

buying: ["vhigh", "high", "med", "low"].
maint: ["vhigh", "high", "med", "low"].
doors: ["2", "3", "4", "5more"].
persons: ["2", "4", "more"].
lug_boot: ["small", "med", "big"].
safety: ["low", "med", "high"]."""

import matplotlib.pyplot as plt
from sklearn import preprocessing, metrics, model_selection
from sklearn import tree
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import math
#LENDO ARQUIVO

itens = pd.read_csv("car.data",encoding = "utf8", header = None)
itens.columns.tolist()
itens.rename(columns = {0:"buying",1:"maint",2:"doors",3:"persons",4:"lug_boot",5:"safety",6:"class"}, inplace = True)

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

ref = ["A","B","C","D"]
refR = ["unacc", "acc", "good", "vgood"]

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

    matrizC = confusion_matrix(y_test, predicts, labels=["unacc", "acc", "good", "vgood"])
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


    matrizC = confusion_matrix(y_test, predicts2, labels=["unacc", "acc", "good", "vgood"])
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

    matrizC = confusion_matrix(y_test, predicts3, labels=["unacc", "acc", "good", "vgood"])
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
