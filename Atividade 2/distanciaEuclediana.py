treino = [[4.4,3.2,1.3,0.2],[4.9,3.1,1.5,0.1],[6.7,3.1,4.4,1.4],[5.6,3.0,4.1,1.3],[7.7,3.8,6.7,2.2],[5.9,3.0,5.1,1.8]]

teste = [[5.4,3.9,1.7,0.4],[6.0,2.2,4.0,1.0],[6.4,3.2,5.3,2.3]]

def distancia(test,train):
    soma = 0
    for j in range(len(test)):
        mult = test[j]-train[j]
        mult = mult**2
        if mult == 0:
            soma += 99999999
        else:
            soma += (1.0/mult)

    dist = soma**(1/2)
    return dist

for k in range(len(teste)):
    test = teste[k]
    print("-------------------------------")
    print("TESTE",str(k)+":")
    for i in range(len(treino)):
        train = treino[i]
        dist = distancia(test,train)
        print("X Treino",i,"=",dist)
