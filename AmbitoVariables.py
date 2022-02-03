print("Hugo\tPaco\tLuis")
hugo=0
paco=1
luis=2

def cajanegra():
    global paco, luis
    luis=paco+hugo
    print("dentro de la caja")
    print(hugo, "\t", paco, "\t", luis)
def funcionPrametrosVariable (*valores):
    return sum(valores)
def funcionRecibeDiccionario (**valores):
    print(valores)
    llaves=valores.keys()
    for x in llaves:
        print(x, ": ",valores[x], end="\t")

def iniciarDatos(datos):

    datos["nombre"]={}
    datos["apellido1"]={}
    datos["apellido2"]={}

def busquedaApellido (almacen, etiqueta, valor):
    return almacen[etiqueta].get(valor)
#recibe varios nombres por el *
def metodoAlmacenar (almacen, *nombresCompleto):
    for nombreCompleto in nombresCompleto:
        nombreDividido=nombreCompleto.split()
        if len(nombreDividido)==2:
            nombreDividido.insert(2,"SinApellido")
        #tupla
        etiquetas="nombre", "apellido1", "apellido2"
        for etiqueta, valor in zip(etiquetas,nombreDividido):
            persona=busquedaApellido(almacen,etiqueta,valor)
            if persona:
                persona.append(nombreCompleto)
            else:
                almacen[etiqueta][valor]=[nombreCompleto]

cajanegra()
print("Fuera de la caja")
print(hugo, "\t", paco, "\t", luis)
print("Funcion con parametros variables")
print(funcionPrametrosVariable(2,3,5,8))
x=funcionPrametrosVariable(8,9,4,3,7,10)
print(type(x))
print("Las funciones pueden recibir diccionarios")
funcionRecibeDiccionario(llave1="cadena",llave2=5,llave3=5.369)
lista =[1,2,3,4]
lista2=["a","b","c"]
print()
print("Funcion Zip une listas ")
objetoIterable=zip(lista,lista2)
for objeto in objetoIterable:
    print(objeto)

misNombre={}
iniciarDatos(misNombre)
metodoAlmacenar(misNombre, "Alejandro Avila Rea", "Erik Avila Rea")
metodoAlmacenar(misNombre, "Luz Hernandez Bautista")
metodoAlmacenar(misNombre, "Elena Vazquez Trujillo")
metodoAlmacenar(misNombre, "Luz Vazquez Vazquez")
print(busquedaApellido(misNombre, "nombre", "Luz"))
print(busquedaApellido(misNombre,"apellido2", "Rea"))