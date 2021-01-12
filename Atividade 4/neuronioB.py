def calcular(neuronio,entrada):
    soma = 0
    d = len(neuronio)
    for k in range(1,d):
        soma += neuronio[k]*float(entrada[k-1])

    if soma > neuronio[0]:
        return 1
    else:
        return 0


def treinarNeuronio(neuronio,treino, ytreino, taxaA = 0.2, e = 0):
    d = len(neuronio)
    limiar = neuronio[0]

    erroTotal = e + 1
    exec = 0
    while (exec < 100):
        for k in range(len(treino)):
            item = treino[k]
            result = calcular(neuronio,item)

            erro = float(ytreino[k]) - result

            if erro**2 > 0:
                for i in range(1,d):
                    neuronio[i] += taxaA*erro*float(item[i-1])

        erroTotal = 0

        for j in range(len(treino)):
            item = treino[j]
            result = calcular(neuronio,item)
            erro = (ytreino[j] - result)**2

            erroTotal += erro

        exec+=1

    return erroTotal

#LEITURA DA BASE
arquivo = open("iris.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []
teste = []
clasT = []
for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])

    itens.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    if clas == "Iris-virginica":
        clas = 1
    else:
        clas = 0
    clasT.append(clas)
    classificacao.append(clas)

arquivo.close()

arquivo = open("irisTeste.data","r", encoding = "utf8")
arq = arquivo.readlines()

for linha in arq:
    t = linha.split(",")
    clas = t[4]
    t.remove(t[4])

    teste.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    if clas == "Iris-virginica":
        clas = 1
    else:
        clas = 0
    clasT.append(clas)

arquivo.close()
total = len(teste)

#INICIAR NEURONIO
import random
neuronio = [0.5, random.random(), random.random(), random.random(), random.random()]
print("Inicial:",neuronio)
errinhos = treinarNeuronio(neuronio,itens,classificacao)
print("Treinado:",neuronio)
print("Erros no treino =",errinhos)

#TESTE
erros = 0
acertos = 0

for k in range(len(teste)):
    item = teste[k]
    pred = calcular(neuronio,item)

    if pred == float(clasT[k]):
        acertos += 1
    else:
        erros += 1

print("ACERTOS:",acertos)
print("ERROS:",erros)
print("Taxa de Acerto:", (acertos/total)*100,"%")
