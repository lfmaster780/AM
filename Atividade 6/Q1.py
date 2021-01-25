"""Class Values:

"unacc", "acc", "good", "vgood"

Attributes:

buying: ["vhigh", "high", "med", "low"].
maint: ["vhigh", "high", "med", "low"].
doors: ["2", "3", "4", "5more"].
persons: ["2", "4", "more"].
lug_boot: ["small", "med", "big"].
safety: ["low", "med", "high"]."""


atributos = [["vhigh", "high", "med", "low"],["vhigh", "high", "med", "low"],["2", "3", "4", "5more"],["2", "4", "more"],["small", "med", "big"],["low", "med", "high"]]
atributosRestantes = [0,1,2,3,4,5]

class Arvore():
    """docstring for Arvore."""

    def __init__(self, raiz, atributo = None):
        self.raiz = raiz
        self.atributo = atributo

    def predict(self,x): #ARRUMAR

        atual = self.raiz
        prox = None
        if len(atual.filhos) > 0:
            prox = atual.filhos[0]

        while prox != None:
            index = -1
            for k in range(len(atual.filhos)):
                filho = atual.filhos[k]
                if filho.valor == x[filho.atributo]:
                    prox = filho
                    index = k
            if index != -1:
                atual = prox

            else:
                prox = None

        predicao = atual.predominancia
        return predicao


class No():
    """docstring for No."""

    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor
        self.filhos = []
        self.predominancia = None

    def addFilho(self,filho):
        self.filhos.append(filho)


def predominancia(y,classificações):
    clas = classificações[0]
    count = [0 for i in range(len(classificações))]

    for k in range(len(y)):
        chave = y[k]
        index = -1
        for i in range(len(classificações)):
            if classificações[i] == chave:
                index = i
                break
        count[index] += 1

    maior = count[0]
    ind = 0
    for c in range(1,len(count)):
        if count[c] > maior:
            ind = c
            maior = count[c]
    pred = classificações[ind]

    return pred

def gerarElementos(x,y,atributo,valor):
    elementosX = []
    elementosY = []

    for k in range(len(x)):
        chave = x[k]
        if chave[atributo] == valor:
            elementosX.append(chave)
            elementosY.append(y[k])

    return elementosX, elementosY;

def calcularErros(y,classificações):
        clas = classificações[0]
        count = [0 for i in range(len(classificações))]

        for k in range(len(y)):
            chave = y[k]
            index = -1
            for i in range(len(classificações)):
                if classificações[i] == chave:
                    index = i
                    break
            count[index] += 1

        maior = count[0]
        ind = 0
        for c in range(1,len(count)):
            if count[c] > maior:
                ind = c
                maior = count[c]

        total = sum(count)
        erros = total - maior
        print(count)
        return erros

def gerarArvore(no, x, y, atributosRestantes, erros = -1):
    no.predominancia = predominancia(y,["unacc", "acc", "good", "vgood"])

    if erros == -1:
        erros = calcularErros(y,["unacc", "acc", "good", "vgood"])

    print("Erro:",erros)
    restantes = []
    for u in atributosRestantes:
        restantes.append(u)
    print("Restantes:",restantes)
    atributos = [["vhigh", "high", "med", "low"],["vhigh", "high", "med", "low"],["2", "3", "4", "5more"],["2", "4", "more"],["small", "med", "big"],["low", "med", "high"]]

    XsYs = [ [] for k in range(len(atributos)) ]
    melhor = erros
    melhorIndex = -1

    for k in range(len(atributosRestantes)):
        atributoAtual = atributosRestantes[k]
        errosAtual = 0
        clas = ""
        print("Atributo:",atributoAtual)

        for i in range(len(atributos[atributoAtual])):
            valorAtual = atributos[atributoAtual][i]
            print("Valor:",valorAtual)
            x1, y1 = gerarElementos(x,y,atributoAtual,valorAtual)
            #print(x1[0],x1[1],y1[0],y1[1])
            erro = calcularErros(y1,["unacc", "acc", "good", "vgood"])
            errosAtual += erro
            XsYs[atributoAtual].append([x1,y1,valorAtual,erro])


        print("Erros atual final:",errosAtual)
        if errosAtual < melhor:
            melhorIndex = atributoAtual
            melhor = errosAtual

    #Checar melhor e gerarArvore recursivamente. e gerar filhos
    print(melhorIndex,melhor)
    if melhorIndex != -1:
        filhos = XsYs[melhorIndex]
        restantes.remove(melhorIndex)
        for f in range(len(filhos)):
            atual = filhos[f]
            novoNo = No(melhorIndex,atual[2])
            print(novoNo.atributo,novoNo.valor,novoNo.filhos)
            print(no.filhos)
            no.filhos.append(novoNo)
            gerarArvore(novoNo,atual[0],atual[1],restantes,atual[3])


    return no

def fitArvore(x,y,atributos = 0):
    no = No(-1,None)
    arvore = Arvore(no)

    atributosR = [k for k in range(atributos)]
    if atributos != 0:
        print("Começar a gerar")
        gerarArvore(arvore.raiz,x,y,atributosR)

    return arvore


#LENDO ARQUIVO

arquivo = open("car.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []

#unacc, acc, good, v-good

for linha in arq:
    t = linha.split(",")
    clas = t[6]
    t.remove(t[6])

    itens.append(t)
    #retirando \n do final da classificacao
    clas = clas[0:len(clas)-1]
    classificacao.append(clas)

total = len(classificacao)
taxes = []
holdouts = 10
for h in range(holdouts):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=0.5)

    tree = fitArvore(X_train,y_train,6)
    print(tree.raiz.predominancia)
    print(tree.raiz.filhos)

    acertos = 0
    erros = 0
    print("======================")
    for k in range(len(X_test)):
        chave = X_test[k]
        pred = tree.predict(chave)

        if pred == y_test[k]:
            acertos += 1
        else:
            erros += 1
    taxa = acertos/(acertos+erros)
    #print("Taxa de Acerto:",taxa*100)
    taxes.append(taxa)

count = 1
for taxas in taxes:
    print("Holdout",count,"->","Taxa de Acerto =",taxas*100,"%")
    count +=1

media = sum(taxes)/len(taxes)
print("")
print("Media =",media*100,"%")
