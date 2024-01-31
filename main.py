# Declarar las variables
G = 6.674e-11 # Constante de gravitación universal
m1 = 5.972e24 # Masa de la Tierra
m2 = 419455 # Masa de la ISS
T = 5559.2 # Periodo orbital de la ISS en segundos

# Calcular el radio de la órbita de la ISS usando la tercera ley de Kepler
r = ((G * m1 * T**2) / (4 * 3.1416**2))**(1/3)

# Definir una función recursiva que calcule la velocidad de la ISS usando el método de Newton-Raphson
def calcular_velocidad(v):
  # Calcular la fuerza centrípeta
  Fc = m2 * v**2 / r
  # Calcular la fuerza gravitatoria
  Fg = G * m1 * m2 / r**2
  # Calcular el error entre las dos fuerzas
  error = Fc - Fg
  # Establecer una tolerancia para el error
  tol = 1e-6
  # Comprobar si el error es menor que la tolerancia
  if abs(error) < tol:
    # Devolver la velocidad
    return v
  else:
    # Calcular la derivada de la fuerza centrípeta con respecto a la velocidad
    dFc = 2 * m2 * v / r
    # Aplicar la fórmula de Newton-Raphson para obtener una mejor aproximación de la velocidad
    v = v - error / dFc
    # Llamar a la función recursiva con la nueva velocidad
    return calcular_velocidad(v)

# Llamar a la función recursiva con una velocidad inicial que quieras

velocidad = calcular_velocidad(1000)

# Mostrar el resultado en la consola
print(f"La velocidad de la ISS es de {velocidad} m/s")