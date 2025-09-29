from ejercicio5_1724110249 import consultar_calificacion
from unittest.mock import patch

def testNormal():
    with patch('builtins.input', side_effect=["2"]):
        resultado = consultar_calificacion(["Leo","Marco","Alan","Mominguez"],[[1.0,2.0,3.0],[2.0,8.0,9.0],[3.0,2.5,6.5],[9.9,9.8,2.0]])
        assert resultado == ("La calificación 2.0 la tienen los alumnos Leo, Marco y Mominguez")

def testStrings():
    with patch('builtins.input', side_effect=["cat","dog","turtle","2"]):
        resultado = consultar_calificacion(["Leo","Marco","Alan","Mominguez"],[[1.0,2.0,3.0],[2.0,8.0,9.0],[3.0,2.5,6.5],[9.9,9.8,2.0]])
        assert resultado == ("La calificación 2.0 la tienen los alumnos Leo, Marco y Mominguez")
