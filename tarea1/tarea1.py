# autor
# fernando rubilar
# Natalia Faundez
# Mario urbina

from mpi4py import MPI
import random

def promedioLista(lista):
    promedio = 0.0
    for i in range(0,len(lista)):
        promedio = promedio + lista[i]
    promedio = promedio/len(lista)
    return promedio

def varianza(lista):
    promedio = 0.0
    suma = 0.0
    promedio = promedioLista(lista)
    for i in range(0,len(lista)):
        suma = suma +(lista[i]**2)-(lista[i]*promedio*2)+(promedio**2)
    varianza = suma/len(lista)
    return varianza

def llenarLista():
    lista= []
    for i in range(0,9):
        lista.append(random.randrange(1,10))
    return   lista

comm = MPI.COMM_WORLD  # comunicador entre dos procesadores #

rank =  comm.rank     # id procesador actual #
size =  comm.size     # tamano procesador #


if rank ==0:
    lista = llenarLista()
    comm.send(lista[0:3],dest=1)
    comm.send(lista[3:6],dest=2)
    comm.send(lista[6:9],dest=3)


if rank ==1:
    lista_recibida = comm.recv(source=0)
    promedioLista2 = promedioLista(lista_recibida)
    varianzaLista2 = varianza(lista_recibida)
    resultado=[]
    resultado.append(promedioLista2)
    resultado.append(varianzaLista2)
    comm.send(resultado, dest =0)
if rank ==2:
    lista_recibida = comm.recv(source=0)
    promedioLista2 = promedioLista(lista_recibida)
    varianzaLista2 = varianza(lista_recibida)
    resultado=[]
    resultado.append(promedioLista2)
    resultado.append(varianzaLista2)
    comm.send(resultado, dest =0)

if rank ==3:
    lista_recibida = comm.recv(source=0)
    promedioLista2 = promedioLista(lista_recibida)
    varianzaLista2 = varianza(lista_recibida)
    resultado=[]
    resultado.append(promedioLista2)
    resultado.append(varianzaLista2)
    comm.send(resultado, dest =0)


if rank==0:
    resultado1 = comm.recv(source=1)
    resultado2 = comm.recv(source=2)
    resultado3 = comm.recv(source=3)
    listaPromedio = []
    listaVarianza = []
    listaPromedio.append(resultado1[0])
    listaPromedio.append(resultado2[0])
    listaPromedio.append(resultado3[0])

    listaVarianza.append(resultado1[1])
    listaVarianza.append(resultado2[1])
    listaVarianza.append(resultado3[1])
    print "Lista : "+str(lista)
    print ""
    for i in range(0, len(listaPromedio)):
        print "promedio lista "+str(i+1)+" : "+str(listaPromedio[i])
        print "Varianza lista "+str(i+1)+" : "+str(listaVarianza[i])

    promedioTotal = promedioLista(listaPromedio)
    varianzaTotal = varianza(lista)

    print "Promedio total : "+str(promedioTotal)
    print "Varianza del arreglo: "+ str(varianzaTotal)
