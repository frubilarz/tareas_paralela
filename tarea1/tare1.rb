require "mpi"
require 'securerandom'

MPI.Init

comm = MPI::Comm::WORLD
size = comm.size
rank = comm.rank

def promedioLista(lista)
  suma = lista.reduce(:+)
  promedio = (suma/lista.size.to_f)
  return promedio
end

def llenarArreglo()
  lista = 100.times.map{SecureRandom.random_number}
  return lista
end

def varianza(lista)
  promedio = promedioLista(lista)
  suma = 0
  for i in 0..lista.size
    suma +=  (lista[i].to_f - promedio.to_f)**2
  end
  s= suma/lista.size
  return s
end

l = llenarArreglo()
promedio = promedioLista(l)

puts l
puts "varianza" + varianza(l).to_s
puts "promedio : "+ promedio.to_s

MPI.Finalize
