def main():
    filas, columnas = tamañoArreglo()
    matriz = crearMatriz(filas,columnas)
    print(f"La suma de los datos ingresados es: {sumarMatriz(matriz)}")

def tamañoArreglo():
    while True:
        try:
            filas = int(input("Ingrese las filas: "))
            if filas < 0 or filas == 0:
                continue
            else:
                break
        except ValueError:
            continue

    while True:
        try:
            columnas = int(input("Ingrese las columnas: "))
            if columnas < 0 or columnas == 0:
                continue
            else:
                break
        except ValueError:
            continue
    return filas, columnas


def crearMatriz(filas, columnas, fila_actual=0, columna_actual=0, matriz=None):
    if matriz is None:
        matriz = []
    if fila_actual == filas:
        return matriz
    if columna_actual == 0:
        matriz.append([])
    while True:
        try:
            n = int(input(f"Ingrese el número en la posición [{fila_actual+1}] [{columna_actual+1}]: "))
            break
        except ValueError:
            continue
    matriz[fila_actual].append(n)
    columna_actual += 1
    if columna_actual == columnas:
        fila_actual += 1
        columna_actual = 0
    return crearMatriz(filas, columnas, fila_actual, columna_actual, matriz)

def sumarMatriz(matriz, suma = 0):
    if len(matriz) == 0:
        return suma
    fila = matriz[0]
    suma += sum(fila)
    return sumarMatriz(matriz[1:],suma)
    
if __name__ == "__main__":
    main()