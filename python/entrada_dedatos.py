contador = 1
total = 0

while contador <= 5:
    print(f"Venta {contador}")
    gasto = int(input("¿Cuánto gastó el cliente? "))
    total = total + gasto
    contador = contador + 1

print(f"Total vendido: ${total}")