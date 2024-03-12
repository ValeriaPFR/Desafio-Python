# Solicitar al usuario que ingrese el precio de suscripción
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))

# Solicitar al usuario que ingrese el número de usuarios
num_usuarios = int(input("Ingrese el número de usuarios: "))

# Solicitar al usuario que ingrese los gastos totales
gastos_totales = float(input("Ingrese los gastos totales: "))

# Solicitar al usuario que ingrese las utilidades de años anteriores
utilidades_anteriores = float(input("Ingrese las utilidades de años anteriores (valores diferentes a 0): "))

# Formula cálculo razón utilidades
utilidades = (precio_suscripcion * num_usuarios - gastos_totales)
razon = utilidades_anteriores/utilidades

# Mostrar resultado
print (f"La razon de las utilidades del proyecto son {razon:.2f}")