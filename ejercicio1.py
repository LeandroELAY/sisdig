def automata(palabra):
  estado_actual = 'e0'
  estados_aceptacion = {'e2'}
  delta = {
      ('e0', 'a'): 'e1',
      ('e1', 'a'): 'e1',
      ('e1', 'c'): 'e2',
      ('e2', 'b'): 'e2'
  }
  for sim in palabra:
      if (estado_actual, sim) in delta:
          estado_actual = delta[(estado_actual, sim)]
      else:
          return False
  return estado_actual in estados_aceptacion


while True:
  palabra = input("Introduce la palabra (a, b, c) o escribe 'exit': ").strip()
  if palabra.lower() == "exit":
      print("Programa finalizado.")
      break

  if automata(palabra):
      print("cadena aceptada")
  else:
      print("cadena rechazada")