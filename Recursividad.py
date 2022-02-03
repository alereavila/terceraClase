def factorila (n):
    if n==0:
        return 1
    else:
        return n*factorila(n-1)
def multiplicacionConSumas (numero, veces):
    if  veces==1:
        return numero
    else:
        return numero+multiplicacionConSumas(numero,veces-1)

def torresHanoi(nDiscos,origen,destino,auxiliar):
    if nDiscos==1:
        print("Mueve el disco 1 de {} a {}".format(origen,destino))
        return
    torresHanoi(nDiscos-1,origen,auxiliar,destino)
    print("Mueve el disco {} del poste {} al poste {}".format(nDiscos,origen,destino))
    torresHanoi(nDiscos-1,auxiliar, destino,origen)



res=factorila(10)
print(res)
multiplicacion = multiplicacionConSumas(7,10)
print(multiplicacion)
print("Torre de Hanoi con recursividad")
discos=3
torresHanoi(discos,"A","B","C")