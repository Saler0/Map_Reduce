def map (k,v):
    return [ (k,(k,v)) , (v,(k,v))   ]
    
def reduce (k, lv ):
    outgoing = []
    incoming = []
    for v in lv:
        if k == v[0]:
            outgoing.append(v[1])
        elif k == v[1]:
            incoming.append(v[0])
    retValue = []
    for o in outgoing:
        for i in incoming:
                retValue.append( i+" -2-> "+o )
    return retValue

exampleInput = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'B'}

print("Input:",exampleInput)

# Fase Mapeo
resultadosMap = []
for key,value in exampleInput.items():
    resultadosMap.append(map(key,value))
print("Resultados map:",resultadosMap)

# Fase de Agrupar y Ordenar
Dic_MergeSort= {"A":[],"B":[],"C":[],"D":[]}
for resulmap in resultadosMap:
    print(resulmap)
    tupla1=resulmap[0]
    Dic_MergeSort[tupla1[0]].append(tupla1[1])
    tupla2=resulmap[1]
    Dic_MergeSort[tupla2[0]].append(tupla2[1])
print("Resultados MergeSort:",Dic_MergeSort)

# Fase reducción
resultadosReuce = []
for key,value in Dic_MergeSort.items():
    resultadosReuce.append(reduce(key,value))
print("Resultados reduce:",resultadosReuce)