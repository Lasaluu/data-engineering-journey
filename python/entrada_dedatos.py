contador = 1
total = 0
venta_mayor = 0
venta_menor = 0

while contador <= 5:
    print(f"Venta {contador}")
    gasto = int(input("¿Cuánto gastó el cliente? "))

    total = total + gasto

    if contador == 1:
        venta_mayor = gasto
        venta_menor = gasto
        
    if gasto > venta_mayor:
        venta_mayor = gasto
    if gasto < venta_menor:
        venta_menor = gasto


    contador = contador + 1

print(f"Total vendido: ${total}")
promedio = total / 5
print(f'El promedio de ventas es de ${promedio}')
print(f"La venta mas grande fue de $ {venta_mayor}")
print(f"La venta mas chica fue de $ {venta_menor}")