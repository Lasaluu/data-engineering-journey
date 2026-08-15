ventas = []
total = 0
ventas_mayor = 0
ventas_menor = 0
promedio = 0

while True:
    venta = int(input("Ingrese cuanto gasto: "))

    if venta == 0:
        break

    ventas.append(venta)


if len(ventas) == 0:
    print("No se ingresaron ventas.")
else:
    ventas_mayor = ventas[0]
    ventas_menor = ventas[0]


for venta in ventas:
    total = total + venta
    if venta > ventas_mayor:
        ventas_mayor = venta
    if venta < ventas_menor:
        ventas_menor = venta

promedio = total / len(ventas)
promedio = round(promedio, 2)

print(f"Este es el total: {total}") 
print(f"Cantidad de ventas: {len(ventas)}")  
print(f"Este es el promedio: {promedio}")
print(f"Esta es la venta mas grande: {ventas_mayor} ")
print(f"Esta es la venta mas chica: {ventas_menor} ")