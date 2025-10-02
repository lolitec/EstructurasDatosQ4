def main():
    alumnos = conseguir_nombres()
    materias = conseguir_materias()
    calificaciones = conseguir_calificaciones(alumnos,materias)
    imprimir_datos(alumnos,materias,calificaciones)
    promalumnos = promedio_alumnos(alumnos,calificaciones)
    prommaterias = promedio_materias(materias,calificaciones)
    imprimir_promedios(alumnos,promalumnos,materias,prommaterias)
    min,max = calif_minmax(calificaciones)
    print(f"La calificación mínima es {min}")
    print(f"La calificación máxima es {max}")
    aprobados,reprobados = cons_aprobados(promalumnos)
    print(f"La cantidad de aprobados es {aprobados}")
    print(f"La cantidad de reprobados es {reprobados}")
    buscar_calificacion(calificaciones)
    promordenado = ordenar_promedios(promalumnos)
    print("Los promedios ordenados de los alumnos: ", end="")
    print(", ".join(f"{prom:.2f}" for prom in promordenado))




def conseguir_nombres():
    alumnos = []
    i = 0
    while i < 10:
        alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
        alumno = alumno.strip().title()
        alumnos.append(alumno)
        i += 1
    return alumnos

def conseguir_materias():
    materias = []
    while True:
        try:
            materia = input("Ingrese la materia: ")
            if materia:
                materia = materia.strip().title()
                materias.append(materia)
            else:
                continue 
        except EOFError:
            print()
            break
    return materias

def conseguir_calificaciones(alumnos,materias):
    calificaciones = []
    for alumno in alumnos:
        califalumnos = []
        for materia in materias:
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificacion para {materia} del alumno {alumno}: "))
                    if calificacion and 0 <= calificacion and calificacion <= 10:
                        califalumnos.append(calificacion)
                        break
                    else:
                        continue
                except ValueError:
                    continue
        calificaciones.append(califalumnos)
    return calificaciones

def imprimir_datos(alumnos,materias,calificaciones):
    for i,alumno in enumerate(alumnos):
        for j,materia in enumerate(materias):
            print(f"{alumno} tuvo {calificaciones[i][j]} en {materia}")

def promedio_alumnos(alumnos,calificaciones):
    promedios = []
    for i in range(len(alumnos)):
        promedio = sum(calificaciones[i])/len(calificaciones[i])
        promedios.append(promedio)
    return promedios

def promedio_materias(materias,calificaciones):
    promedios = []
    for i,materia in enumerate(materias):
        califmateria = 0
        for calificacion in calificaciones[i]:
            califmateria += calificacion
        promedio = califmateria / len(calificaciones[i])
        promedios.append(promedio)
    return promedios

def imprimir_promedios(alumnos, promalumnos, materias, prommaterias):
    for i in range(len(alumnos)):
        print(f"El alumno {alumnos[i]} tiene un promedio de {promalumnos[i]:.2f}")
    
    for i in range(len(materias)):
        print(f"La materia {materias[i]} tiene un promedio de {prommaterias[i]:.2f}")

def calif_minmax(calificaciones):
    min = 10
    max = 0
    for alumno in calificaciones:
        for calificacion in alumno:
            if calificacion > max:
                max = calificacion
            elif calificacion < min:
                min = calificacion
            else:
                continue
    return min,max

def cons_aprobados(promedios):
    aprobados = 0
    reprobados = 0
    for promedio in promedios:
        if promedio >= 7:
            aprobados += 1
        else:
            reprobados += 1
    return aprobados,reprobados
    
def buscar_calificacion(calificaciones):
    while True:
        try:
            califbusq = float(input("Ingrese la calificación a buscar: "))
            break
        except ValueError:
            continue
    
    encontrada = False
    for alumno in calificaciones:
        if califbusq in alumno:
            encontrada = True
            break

    if encontrada:
        print(f"La calificación {califbusq} se encuentra en el arreglo.")
    else:
        print(f"La calificación {califbusq} no se encuentra en el arreglo.")


def ordenar_promedios(promedios):
    ordenado = sorted(promedios,reverse=True)
    return ordenado

if __name__ == "__main__":
    main()