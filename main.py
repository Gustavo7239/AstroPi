# Declaramos las variables con los valores de las constantes
G = 6.674e-11 # Constante de gravitación universal
M = 5.972e24 # Masa de la Tierra
R = 6.371e6 # Radio de la Tierra
H = 400e3 # Altura de la ISS sobre la superficie terrestre

# Definimos una función que calcula la velocidad orbital de la ISS
def velocidad_orbital():
  # Calculamos el radio de la órbita de la ISS
  r = R + H
  # Aplicamos la fórmula de la velocidad orbital
  v = (G * M / r) ** 0.5
  # Devolvemos el valor de la velocidad
  return v

# Llamamos a la función y guardamos el resultado en una variable
v_iss = velocidad_orbital()

# Imprimimos la velocidad en la consola con un mensaje
print(f"La velocidad orbital de la ISS es de {v_iss} m/s")
