from mpi4py import MPI
import random, decimal
import numpy
import time
t0 = time.time()

comm = MPI.COMM_WORLD #comunicador entre dos procesadores
size = comm.Get_size() #cantidad de procesadores
rank = comm.Get_rank()#id procesador actual

def diferencias(lista, promedio):
    suma = 0.0
    for i in range(0,len(lista)):
        suma=suma + ((promedio- lista[i])**2)
    return suma

if rank == 0:
	lista= numpy.random.uniform(0,1,100) #devuelve una lista de 100 datos con distribucion de 0 a 1
	print "la lista inicial es: "+ str(lista) 
	lista_par=array_split(lista, size) #Divida la lista dada en la cantidad de procesadores 
else:
	lista= None


repa= comm.scatter(lista_par,root=0) #hace el scatter que consiste en repartir la listan entre los procesadores
for i in range(0,size):
    if rank==i:    	
        lista = repa.get('lista_par')
        promedio = numpy.mean(lista_par)
        repartir=comm.gather(promedio, root=0) #recoge las listas repartidad de cada procesador y la devuelve al madre

if rank==0:
	print "lista : " +str(data.get('lista'))        
    t1 = time.time()
    print "el tiempo de ejecucion es ",t1-t0



