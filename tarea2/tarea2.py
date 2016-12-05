#author: Fernando Rubilar
#        Natalia Faundez
#
from mpi4py import MPI
import random, decimal
import numpy

comm = MPI.COMM_WORLD #comunicador entre dos procesadores
size = comm.Get_size() #cantidad de procesadores
rank = comm.Get_rank()#id procesador actual

def diferencias(lista, promedio): 
    suma = 0.0
    for i in range(0,len(lista)):
        suma=suma + ((promedio- lista[i])**2)
    return suma

def promedioLista(lista):
    promedio = 0.0
    for i in range(0,len(lista)):
        promedio = promedio + lista[i]
    promedio = promedio/len(lista)
    return promedio

if rank == 0:
   lista= numpy.random.uniform(0,1,100) #devuelve una lista de 100 datos con distribucion de 0  1
   promedioGeneral = promedioLista(lista) #promedio de la lista
   d = dict(lista=lista,promedio = promedioGeneral) #define el objeto de, para tener guardadas las listas con su respectivo promedio
else:
   d = None
   
data = comm.bcast(d, root=0)#hace el bcast y lo deja definido como objeto en cada procesador (objetos iguales)
for i in range(0,size):
    if rank==i:
        promedio = data.get('promedio') 
        lista = data.get('lista') 
        termino= i*(100/(size-1)) #divide el largo del arreglo de la lista en la cantidad de procesadores 
        #y lo multiplica por el procesador actual, asi se obtiene la posicion final de cada lista modificado
        inicio = termino-(100/(size-1))# se calcula el inicio de la lista nueva
        if 100%size==0 and (i+1)==size:
             varianza = diferencias(lista[inicio:termino+1],promedio)
        else:
             varianza = diferencias(lista[inicio:termino+1],promedio)
        buf_list = comm.gather(varianza, root=0)# recoge las varianzas de cada procesador y las envia al procesador madre


if rank==0:
    print buf_list
