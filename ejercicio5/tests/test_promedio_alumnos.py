from ejercicio5_1724110249 import promedio_alumnos

def testPromedioAlumnos():
    resultado = promedio_alumnos([[5.0,4.0,6.0],[7.0,9.0,2.0]])
    assert resultado == [5.0,6.0]