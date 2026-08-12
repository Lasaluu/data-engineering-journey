total = 0
cantidad_de_gastos = 0

while True:
    pedir_gasto = int(input("Ingese cuanto gasto: "))

    if pedir_gasto == 0:
        break

    else:
        cantidad_de_gastos = cantidad_de_gastos + 1
        total = total + pedir_gasto
        promedio = round (total / cantidad_de_gastos, 2)

        print("Registrado")
        print (f"El total es: {total}")
        print(f"Cantidad de gastos: {cantidad_de_gastos}")
        print(f"Promedio de gasto: ${promedio}")


if cantidad_de_gastos == 0:
    print("No se ingresaron gastos")

else:

    print("----- RESUMEN FINAL -----")
    print(f"Total gastado: ${total}")
    print(f"Cantidad de gastos: {cantidad_de_gastos}")
    print(f"Promedio final: ${promedio}")  