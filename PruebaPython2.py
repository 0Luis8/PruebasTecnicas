"""
 * Crea una función que encuentre todas las combinaciones de los números
   de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
     y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
     una vez cada elemento de la lista (pero pueden existir
     elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 * - Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
     (Si no existen combinaciones, retornar una lista vacía)
 """

def find_sums(numbers: list, target: int) -> list:
  # Función interna que utiliza backtracking para encontrar combinaciones
  def backtracking(start: int, target: int, combination: list):
    
    # Si el target llega a 0, se ha encontrado una combinación válida
    if target == 0:
      result.append(combination[:])# Se añade una copia de "combination" actual a  "result"
      return
    # Si el target es menor que 0 o hemos recorrido todos los números que hay en "numbers", NO HAY SOLUCION
    if target < 0 or start == len(numbers):
      return
    # búsqueda
    # Pruebo las opciones desde el índice actual hacia adelante
    for index in range(start, len(numbers)):
      # Se evita duplicados consecutivos (si ya hemos usado este número en esta posición)
      if index > start and numbers[index] == numbers[index - 1]:
        continue
      # Se incluye el número actual en "combination"
      combination.append(numbers[index])
      # Llamada recursiva con el siguiente índice y el nuevo "target" actualizado
      backtracking(index + 1, target - numbers[index], combination)
      # Eliminación del último número añadido para explorar otras combinaciones
      combination.pop()

  # Ordeno numbers para manejar los duplicados correctamente
  numbers.sort()
  result = []# Aquí guardo todas las combinaciones válidas
  backtracking(0, target, [])# Llamada inicial a backtracking()
  return result# Devolvemos todas las combinaciones válidas encontradas


print(find_sums([1, 5, 3, 2], 6))
print(find_sums([1, 1, 3, 4, 2, 2, 1, 3], 6))
