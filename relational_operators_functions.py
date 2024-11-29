class map_reduce_Union:
    def __init__(self,table_T,table_S):
        # Guardar las tablas T y S como atributos de la clase
        self.table_T = table_T
        self.table_S = table_S

    def map_Union(self):
        # Emitir las filas de ambas tablas
        self.mapped_data = [] 
        for key, value in self.table_T.items():
            self.mapped_data.append((key, value))  
        for key, value in self.table_S.items():
            self.mapped_data.append((key, value))
        return self.mapped_data

    def reduce_Union(self):
        # combinar las filas eliminando duplicados
        data_output = {} # Diccionario que almacenara resultados únicos
        for key, value in self.mapped_data:
            if key not in data_output:
                data_output[key] = set()  # set() para evitar duplicados de valores
            data_output[key].add(value)  # Añadir el valor al set de la clave
        # Imprimir el resultado de la unión
        print("Resultado de la unión (sin duplicados):")
        print(data_output)

class map_reduce_Difference:
    def __init__(self,table_T,table_S):
        # Guardar las tablas T y S como atributos de la clase
        self.table_T = table_T
        self.table_S = table_S

    def map_Difference(self):
        # Emitir las filas de ambas tablas con una referencia en la clave indicando a que tabla pertenecia
        self.mapped_data = []
        for key, value in self.table_T.items():
            self.mapped_data.append(('T', f"{key}_{value}"))  # crea un key que referencia si es de T
        for key, value in self.table_S.items():
            self.mapped_data.append(('S', f"{key}_{value}"))  # crea un key que referencia si es de S
        return self.mapped_data
    
    def reduce_Difference(self):
        data_output = {} # Diccionario que almacenara los valores de T que no esten en S
        s=[]
        t=[]
        for keymap, valuemap in self.mapped_data:
            if keymap == 'T':
                t.append(valuemap)
            else:
                s.append(valuemap)
        difference=[valuemap for valuemap in t if valuemap not in s] # deja solo lo de t que no este en s
        #regresando a un diccionario
        for valuemap in difference:
            key , value = valuemap.split('_', 1)
            data_output[key]=value
        # Imprimir el resultado de la unión
        print("Resultado de la interseccion:")
        print(data_output)


class map_reduce_Intersection:
    def __init__(self,table_T,table_S):
        # Guardar las tablas T y S como atributos de la clase
        self.table_T = table_T
        self.table_S = table_S
    def map_Intersection(self):
        # Emitir las filas de ambas tablas con una referencia en la clave indicando a que tabla pertenecia
        self.mapped_data = []
        for key, value in self.table_T.items():
            self.mapped_data.append(('T', f"{key}_{value}"))  # crea un key que referencia si es de T
        for key, value in self.table_S.items():
            self.mapped_data.append(('S', f"{key}_{value}"))  # crea un key que referencia si es de S
        return self.mapped_data
    def reduce_Intersection(self):
        data_output = {} # Diccionario que almacenara la interseccion de tT con S
        s=[]
        t=[]
        for keymap, valuemap in self.mapped_data:
            if keymap == 'T':
                t.append(valuemap)
            else:
                s.append(valuemap)
        difference=[valuemap for valuemap in t if valuemap in s] # deja solo lo de t que esten en s
        #regresando a un diccionario
        for valuemap in difference:
            key , value = valuemap.split('_', 1)
            data_output[key]=value
        # Imprimir el resultado de la unión
        print("Resultado de la diferencia:")
        print(data_output)


# Representación como diccionarios clave-valor tablas T y S
T = {'A': 1, 'B': 2, 'C': 1, 'D': 9, 'E':4}
S = {'A': 4, 'B': 2, 'C': 5, 'D': 9, 'E':3}

print("Tabla T:", T)
print("Tabla S:", S)

print("== Hacer Map-Reduce Union ==")
union = map_reduce_Union(T,S)
union.map_Union()
union.reduce_Union()


print("== Hacer Map-Reduce Difference ==")
difference = map_reduce_Difference(T,S)
difference.map_Difference()
difference.reduce_Difference()

print("== Hacer Map-Reduce Intersection ==")
intersection = map_reduce_Intersection(T,S)
intersection.map_Intersection()
intersection.reduce_Intersection()