def validarIngresoEntero(leyenda):
  while True:
    try:
      entero = int(input(leyenda))  
      break
    except ValueError:
      print("El numero debe ser entero")
  return entero