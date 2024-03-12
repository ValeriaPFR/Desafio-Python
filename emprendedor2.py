# Solicitar al usuario que ingrese el precio de suscripción
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))

# Solicitar al usuario que ingrese el número de usuarios normales
num_usuarios = int(input("Ingrese el número de usuarios: "))

# Solicitar al usuario que ingrese el número de usuarios premium
num_premium = int(input("Ingrese el número de usuarios premium: "))

# Solicitar al usuario que ingrese los gastos totales
gastos_totales = float(input("Ingrese los gastos totales: "))

# Solicitar al usuario que ingrese los gastos totales
ingreso_premium = (precio_suscripcion * num_premium * 1.5)

# Fórmula cálculo utilidades
utilidades = (precio_suscripcion * num_usuarios + ingreso_premium - gastos_totales)

# Mostrar resultado
print (f"Las utilidades del proyecto son {utilidades}")