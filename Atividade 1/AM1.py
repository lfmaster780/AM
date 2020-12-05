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

#classificando com as regras
total = len(classificacao)
acertos = 0
predicao = []

for k in range(total):
    atual = itens[k]
    pred = ""

    if atual[0] == "vhigh":
        pred = "unacc"

    elif atual[0] == "high":
        if atual[1] == "vhigh" or atual[5] != "high":
            pred = "unacc"
        else:
            pred = "acc"

    elif atual[0] == "med":
        if atual[5] == "high":
            if atual[4] == "big" or atual[4] == "med":
                pred = "vgood"
            else:
                pred = "acc"
        else:
            pred = "unacc"

    else:
        if atual[3] == "4" or atual[3] == "more":
            if atual[4] == "big" and atual[5] == "high":
                pred = "vgood"
            elif (atual[4] == "big" and atual[5] == "med") or (atual[4] == "med" and atual[5] == "high"):
                pred = "good"
            elif atual[4] == "med" and atual[5] == "med":
                pred = "acc"
            else:
                pred = "unacc"
        else:
            pred = "unacc"

    if pred == classificacao[k]:
        acertos += 1

    predicao.append(pred)

print("ACERTOS:",acertos)
print("ERROS:",total-acertos)
taxa = (acertos/total)*100
print("Taxa de Acerto:",taxa,"%")
