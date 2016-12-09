#problema3 se define una lista en un procesador (madre), se reparte mediante scatter en todos particionando la lista
#en cada procesador se calcula el promedio y se devuelve al madre mediante gather, se saca la media y mediante bcast se reparte 
#a todos los nodos y mediante scatter se reparten los promedio de cada lista nuevamente??(nando esta parte no la entiendo muy bien) y 
#se valcula varianza en cada procesador se envia mediante gather y se saca varianza en el nodo madre

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
	listapar=array_split(lista, size) #divide la lista dada en la cantidad de procesadores -->no estoy muy segura de 
	#aplicarlo aca y en el archivo del ayudante aparece listapar.array_split creo que deberia 
	
else:
	lista= None


repa= comm.scatter(listapar,root=0) #hace el scatter que consiste en repartir la lista entre los procesadores
for i in range(0,size):
    if rank==i:    	
        promedio = numpy.mean(listapar)
        repartir=comm.gather(promedio, root=0) #recoge los promedios de cada procesador y la devuelve al madre

if rank==0:
    suma = 0
    for i in range(0,size):
        suma = suma + repartir[i] #suma los promedios de cada procesador 
    media = suma/size #calculo del promedio--->no se si deberia ser dividido en la variable 100 o en size

#hasta la parte donde hay que hacer bcast y repartir a todos     
    

