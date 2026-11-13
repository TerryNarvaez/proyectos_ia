cartas = [7, 2, 5]

pos = 1
while pos < len(cartas):
    k = pos
    while k > 0 and cartas[k - 1] > cartas[k]:
        temp = cartas[k]
        cartas[k] = cartas[k - 1]
        cartas[k - 1] = temp
        k = k - 1
    pos = pos + 1

print(cartas)


valores = [99, 2737237, 283823832, 666, 67, 1]

hubo_cambio = True
limite = len(valores) - 1
while hubo_cambio:
    hubo_cambio = False
    for p in range(limite):
        if valores[p] > valores[p + 1]:
            aux = valores[p]
            valores[p] = valores[p + 1]
            valores[p + 1] = aux
            hubo_cambio = True
    limite = limite - 1

print(valores)
