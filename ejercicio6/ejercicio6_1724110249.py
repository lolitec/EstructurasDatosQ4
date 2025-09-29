## Diseñe un programa que realize:
## Declare y cree un arreglo con edades de un grupo de personas
## Calcule e imprima la edad minima y máxima del grupo de personas con su nombre, el promedio de las edades y la mediana del grupo
## Permita al usuario agregar una nueva edad al arreglo y mostrar nuevamente los datos actualizados
def main():
    personas = cons_num_personas()
    edades = cons_edades(personas)
    min = edad_minima(edades)
    max = edad_maxima(edades)
    promedio = promedio_edades(edades)
    mediana = mediana_edades(edades)
    imp_resultados(min,max,promedio,mediana)
    nueva_edad(edades)
    min = edad_minima(edades)
    max = edad_maxima(edades)
    promedio = promedio_edades(edades)
    mediana = mediana_edades(edades)
    imp_resultados(min,max,promedio,mediana)

def cons_num_personas():
    while True:
        try:
            personas = int(input("Ingrese el numero total de personas del grupo: "))
            if personas < 0 or personas == 0:
                continue
            else:
                break
        except (ValueError,TypeError):
            continue
    return personas

def cons_edades(n):
    edades = []
    i = 0
    while i < n:
        try:
            edad = int(input(f"Ingrese la edad de la {i+1}° persona: "))
            edades.append(edad)
            i += 1
        except (ValueError,TypeError):
            continue
    return edades

def edad_minima(edades):
    min = edades[0]
    for i in edades:
        if i < min:
            min = i
    return min

def edad_maxima(edades):
    max = edades[0]
    for i in edades:
        if i > max:
            max = i
    return max

def promedio_edades(edades):
    promedio = round(sum(edades)/len(edades),1)
    return promedio

def mediana_edades(edades):
    edadesOrdenadas = sorted(edades)
    n = len(edadesOrdenadas)
    if n % 2 == 0:
        mediana = (edadesOrdenadas[n//2 - 1] + edadesOrdenadas[n//2]) / 2
    else:
        mediana = edadesOrdenadas[n//2]
    return mediana

def imp_resultados(min,max,promedio,mediana):
    print(f"La edad mínima es: {min}")
    print(f"La edad máxima es: {max}")
    print(f"El promedio de las edades es: {promedio}")
    print(f"La mediana de las edades es: {mediana}")

def nueva_edad(edades):
    while True:
        try:
            edad = int(input("Ingrese la nueva edad: "))
            if edad > 0:
                break
            else:
                continue
        except (ValueError,TypeError):
            continue
    return edades.append(edad)



if __name__ == "__main__":
    main()