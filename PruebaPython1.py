"""
  1.- /*

  Escribe una función que reciba un texto y retorne verdadero o
  falso (Boolean) según sean o no palíndromos.
  Un Palíndromo es una palabra o expresión que es igual si se lee
  de izquierda a derecha que de derecha a izquierda.
  NO se tienen en cuenta los espacios, signos de puntuación y tildes.
  Ejemplo: Ana lleva al oso la avellana. # TRUE

"""

def es_palindromo(texto):
    # Listo todas las vocales con tildes para reemplazarlas
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
              'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'}
    
    # Reemplazo las tildes y paso todo a minúsculas
    texto = ''.join(tildes.get(c, c) for c in texto).lower()
    
    # Elimino caracteres no alfanuméricos
    limpio = ''.join(c for c in texto if c.isalnum())
    
    # Compruebo si el texto limpio es igual en sentido contrario (la comparación ya devuelve un boolean)
    return limpio == limpio[::-1]:

print(es_palindromo("Ana lleva al oso la avellana."))  # True


"""
  2.-

  Escribe una función que calcule y retorne el factorial de un número dado
  de forma recursiva.

"""

def factorial(n):
    # Compruebo que el número introducido sea negativo
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    # Esto sería el caso base, con el mismo resultado de 1
    if n == 0 or n == 1:
        return 1

  # Multiplico el número facilitado por el factorail(numero justamente inferior) [Recursividad]
    return n * factorial(n - 1)


"""
  3.-

  Escribe una función que calcule si un número dado es un número de Armstrong
  (o también llamado narcisista).
  Si no conoces qué es un número de Armstrong, debes buscar información
  al respecto.

"""

def es_armstrong(n):
    # Conversión del número a cadena para poder recorrer cada dígitos
    digitos = str(n)
    # Calculo cuantas cifras tiene "n"
    num_cifras = len(digitos)
    
    # Hago la suma de los factoriales de cada cifra
    suma = sum(int(d)**num_cifras for d in digitos)
    
    # Comparo ambos números para ver si son iguales
    if suma == n:
      return "Este es un número de Amstrong"
    else:
      return "Este es un número normal"
