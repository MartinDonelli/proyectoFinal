
from decoraciones import decorar
from gestion import obtenerAnimales, agregarAnimal

listadoAnimales = obtenerAnimales("animales.dat")
print(listadoAnimales)
while True:
  print(
    f'''
    \t Menu
    [1] Agregar un animal
    [2] Modificar un animal
    [3] Eliminar un animal
    [0] Salir
    '''
    )
  opcion = int(input("Selecccione una opcion: "))
  if opcion == 0:
    break
  elif opcion == 1:
    decorar()
    print("Agregar")
    agregarAnimal(listadoAnimales)
  elif opcion == 2:
    decorar()
    print("Modificar")
  elif opcion == 3:
    decorar()
    print("Eliminar")
  else:
    decorar()
    print("Elija una opcion correcta")

print(listadoAnimales)
