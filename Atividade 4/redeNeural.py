import numpy as np

from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.optimizers import Adam
import pandas

dataframe = pandas.read_csv("wine.csv", delimiter=",", header=None)
dataset = dataframe.to_numpy()

X = dataset[:,1:3].astype(float)
y = dataset[:,0]

#Inicio
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
bin_y = np_utils.to_categorical(encoded_Y)

#Dividir treino e teste
from sklearn.model_selection import train_test_split
acuracias = []
for r in range(30):
    X_train,X_test,y_train,y_test=train_test_split(X,bin_y,train_size=0.5,random_state=2)

    model=Sequential()

    model.add(Dense(9, input_dim=2, activation="relu"))
    model.add(Dense(6, activation="sigmoid"))
    model.add(Dense(3, activation="softmax"))

    opt = SGD(learning_rate=0.2)
    model.compile(optimizer=opt,loss="categorical_crossentropy",metrics=["accuracy"])


    model.fit(X_train,y_train,epochs=500, verbose=0)
    loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
    print("Taxa de Acerto = {:.2f}".format(accuracy))
    acuracias.append(accuracy)
    #print(f'predict:{model.predict(X_test)}')
    #print("YTEST:",y_test)

print("-----------------------------------------")
media = sum(acuracias)/len(acuracias)
print("Media:",media*100,"%")
som = 0
for g in range(len(acuracias)):
    quadrado = (acuracias[g]-media)**2
    som += quadrado

som = som/len(acuracias)
desvio = som**(1/2)

print("Desvio Padrao:",desvio*100,"%")

#print(acuracias)
