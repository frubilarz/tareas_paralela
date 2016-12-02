from mpi4py import MPI
import random, decimal
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

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
   lista=s = numpy.random.uniform(0,1,100)
   promedioGeneral = promedioLista(lista)
   d = dict(lista=lista,promedio = promedioGeneral)
else:
   d = None
data = comm.bcast(d, root=0)
for i in range(0,size):
    if rank==i:
        promedio = data.get('promedio')
        lista = data.get('lista')
        buf_list = comm.gather(promedio, root=0)


if rank==0:
    print buf_list
