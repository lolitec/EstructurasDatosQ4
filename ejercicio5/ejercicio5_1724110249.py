## Busqueda de elementos en un arreglo: Diseñe un programa que
## 1. Permita declarar y crear un arreglo con calificaciones de un grupo de estudiantes, ints (0-100)
## 2. Calcule el promedio de las calificaciones de cada alumno y de las calificaciones almacenadas en el arreglo.
## 3. Que permita buscar si una calificacion especifica (Ingresada por el usuario) se encuentra en el arreglo.
## 4. Que muestre los resultados de forma clara en la pantalla.
## Inputs: n de alumons del grupo,n de materias,alumno,calificaciones
## Despues de conseguir los promedios se pregunta al usuario por una calificacion especifica y se listan los alumnos que la tienen
import inflect

Inflect = inflect.engine()
def main():
    numAlumnos = cons_num_alumnos()
    numMaterias = cons_num_materias()
    nombresAlumnos = cons_nombre_alumno(numAlumnos)
    califAlumnos = calificaciones_alumnos(numAlumnos,numMaterias,nombresAlumnos)
    promAlumnos = promedio_alumnos(califAlumnos)
    promGrupal = promedio_grupal(promAlumnos)
    imp_resultados(nombresAlumnos, promAlumnos,promGrupal)
    print(consultar_calificacion(nombresAlumnos,califAlumnos))
    
def cons_num_alumnos():
    while True:
        try:
            n = int(input("Ingrese el número de alumnos del grupo TI41: "))
            if n < 0:
                continue  
            elif n == 0:
                continue
            else:
                break
        except (ValueError, TypeError):
            continue
    return n

def cons_nombre_alumno(alumnos):
    nombres = []
    for i in range(alumnos):
        while True:
            nombreAlumno = input(f"Ingrese el nombre del alumno {i+1}: ")
            if nombreAlumno and nombreAlumno.isalpha():
                nombres.append(nombreAlumno)
                break
            else:
                continue
    return nombres

def cons_num_materias():
    while True:
        try:
            n = int(input("Ingrese el número de materias del grupo TI41: "))
            if n < 0 or n == 0:
                continue
            else:
                break
        except (ValueError,TypeError):
            continue
    return n

def calificaciones_alumnos(alumnos,materias,nombres):
    calificaciones = []
    for i in range(alumnos):
        alumno = []
        for j in range(materias):
            while True:
                try:
                    calif = float(input(f"Ingrese la calificación del alumno {nombres[i]} para la materia {j+1}: "))
                    if calif >= 0 and calif <= 100:
                        alumno.append(calif)
                        break
                    else:
                        continue
                except (ValueError, TypeError):
                    continue
        calificaciones.append(alumno)
    return calificaciones

def promedio_alumnos(calificaciones):
    promedios=[]
    for i in calificaciones:
        promedio = sum(i)/len(i)
        promedios.append(promedio)
    return promedios

def promedio_grupal(promedios):
    promedio = sum(promedios)/len(promedios)
    return promedio

def imp_resultados(alumnos,promAlumnos,promGrupal):
    for i in range(len(alumnos)):
        print(f"El promedio del alumno {alumnos[i]} es {promAlumnos[i]}")
    print(f"El promedio del grupo Ti41 es: {promGrupal}")

def consultar_calificacion(alumnos,calificaciones):
    indices = []
    alumBusq = []
    valido = False
    while True:
        try:
            busq = float(input("Ingrese la calificación que desea buscar: "))
            for i in calificaciones:
                if busq in i:
                    valido = True
                    break
            if valido:
                break
            else:
                print("Ningun alumno tiene asignada esa calificación")
                continue
        except (ValueError,TypeError):
            continue
    for i, cal in enumerate(calificaciones):
        if busq in cal:
            indices.append(i)
    for i in indices:
        alumBusq.append(alumnos[i])
    alumStr = Inflect.join(alumBusq).replace("and", "y").replace(", y", " y")
    return f"La calificación {busq} la tienen los alumnos {alumStr}"

if __name__ == "__main__":
    main()
