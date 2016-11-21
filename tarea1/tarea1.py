from mpi4py import MPI
import random

def promedio_varianza(lista):
    promedio = 0.0
    suma = 0
    promedio = (lista[0]+lista[1]+lista[2])/3.0
    for i in range(0,3):
        suma = suma +(lista[i]-promedio)**2
    varianza = suma/3.0
    resultado =[promedio,varianza,lista]
    return resultado

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
    resultado = promedio_varianza(lista_recibida)
    comm.send(resultado, dest =0)

if rank ==2:
    lista_recibida = comm.recv(source=0)
    resultado = promedio_varianza(lista_recibida)
    comm.send(resultado, dest =0)

if rank ==3:
    lista_recibida = comm.recv(source=0)
    resultado = promedio_varianza(lista_recibida)
    comm.send(resultado, dest =0)



if rank==0:
    resultado1 = comm.recv(source=1)
    resultado2 = comm.recv(source=2)
    resultado3 = comm.recv(source=3)
    listafinal = []
    listafinal.append(resultado1[0])
    listafinal.append(resultado2[0])
    listafinal.append(resultado3[0])

    listaresultante = promedio_varianza(listafinal)
    print "lista 1:     "+str(resultado1[2])
    print "promedio lista 1:  "+str(resultado1[0])
    print "varianza lista 1:  "+str(resultado1[1])

    print "lista 2:     "+str(resultado2[2])
    print "promedio lista 2:  "+str(resultado2[0])
    print "varianza lista 2:  "+str(resultado2[1])

    print "lista 3:     "+str(resultado3[2])
    print "promedio lista 3:  "+str(resultado3[0])
    print "varianza lista 3:  "+str(resultado3[1])

    print "lista final promedio:   " +str(listaresultante[0])
    print "lista final varianza:  " +str(listaresultante[1])
