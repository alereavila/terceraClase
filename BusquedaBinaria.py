def busquedaBinaria( arreglo, valor, inferior=0,superior=None):
    if superior==None:
        superior=len(arreglo)-1

    if superior>=inferior:
        medio=(inferior+superior)//2
        if arreglo[medio]==valor:
            return medio
        elif valor < arreglo[medio]:
            return busquedaBinaria(arreglo,valor,inferior, medio-1)
        else:
            return busquedaBinaria(arreglo,valor,medio+1, superior)
    else:
        #elemento no presente en el arreglo
        return -1

seq=[34,67,8,123,4,100,95,10]
print(seq)
seq.sort()
print(seq)
print(busquedaBinaria(seq,100))
