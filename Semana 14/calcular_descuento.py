# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento):
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Inicialización del programa
#Entrada de datos, pide al usuario ingresar dos valores, el momento total de la compra y el porcentaje de descuento.
#Calculo_del descuento:toma el monto total y el porcentaje .
# Imprime la Primera compra
print("Primera compra:")
monto_total_1 = float(input("Introduce el monto total de la compra: "))
porcentaje_descuento_1 = float(input("Introduce el porcentaje de descuento: "))
descuento_1, monto_final_1 = calcular_descuento(monto_total_1, porcentaje_descuento_1)
print(f"\nResultado de la Primera Compra:")
print(f"Porcentaje de descuento: {porcentaje_descuento_1}%")
print(f"Descuento aplicado: ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final_1:.2f}\n")
# Inicialización del programa
#Entrada de datos, pide al usuario ingresar dos valores, el momento total de la compra y el porcentaje de descuento.
#Calculo_del descuento:toma el monto total y el porcentaje .
# Imprime Segunda compra
print("Segunda compra:")
monto_total_2 = float(input("Introduce el monto total de la compra: "))
porcentaje_descuento_2 = float(input("Introduce el porcentaje de descuento: "))
descuento_2, monto_final_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
print(f"\nResultado de la Segunda Compra:")
print(f"Porcentaje de descuento: {porcentaje_descuento_2}%")
print(f"Descuento aplicado: ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final_2:.2f}")


