def map (k,v):
    return [ (k,([k,k],[v,k])) ]

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
            if o != 'A':
                retValue.append( i+" -2-> "+o )
            else:
                retValue.append(o+" -2-> C")
    return retValue

exampleInput = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'B'}

print("Input:",exampleInput)

# Fase Mapeo
resultadosMap = []
for key,value in exampleInput.items():
    resultadosMap.append(map(key,value))
print("Resultados map:",resultadosMap)

# Fase reducción
resultadosReuce = []
for resulmap in resultadosMap:
    tupla=resulmap[0]
    resultadosReuce.append(reduce(tupla[0],tupla[1]))
print("Resultados reduce:",resultadosReuce)